from datetime import datetime, timedelta

from backend.app.models.customer import Customer
from backend.app.models.session import Session

from backend.app.core.security import (
    hash_password,
    verify_password
)

from backend.app.core.jwt_handler import (
    create_access_token,
    create_refresh_token
)

from backend.app.core.config import settings

from backend.app.utils.validators import (
    validate_password
)

from backend.app.core.exceptions import (
    UserAlreadyExists,
    InvalidCredentials
)

from backend.app.core.logger import logger


class AuthService:

    def register(
        self,
        db,
        user_data
    ):
        """
        Register a new customer.
        """

        # Check if user already exists
        existing_user = (
            db.query(Customer)
            .filter(
                Customer.email == user_data.email
            )
            .first()
        )

        if existing_user:
            logger.warning(
                f"Registration failed. User already exists: {user_data.email}"
            )
            raise UserAlreadyExists()

        # Validate password
        validate_password(
            user_data.password
        )

        # Create user
        user = Customer(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            phone=user_data.phone,
            password_hash=hash_password(
                user_data.password
            )
        )

        try:
            db.add(user)
            db.commit()
            db.refresh(user)

            logger.info(
                f"User registered successfully: {user.email}"
            )

            return user

        except Exception as e:
            db.rollback()

            logger.error(
                f"Registration failed: {str(e)}"
            )

            raise e

    def login(
        self,
        db,
        email: str,
        password: str
    ):
        """
        Authenticate user and generate tokens.
        """

        user = (
            db.query(Customer)
            .filter(
                Customer.email == email
            )
            .first()
        )

        if not user:
            logger.warning(
                f"Invalid login attempt: {email}"
            )
            raise InvalidCredentials()

        if not verify_password(
            password,
            user.password_hash
        ):
            logger.warning(
                f"Invalid login attempt: {email}"
            )
            raise InvalidCredentials()

        # Generate access token
        access_token = create_access_token(
            {
                "sub": str(
                    user.customer_id
                ),
                "role": user.role
            }
        )

        # Generate refresh token
        refresh_token = create_refresh_token(
            {
                "sub": str(
                    user.customer_id
                )
            }
        )

        expire_date = (
            datetime.utcnow()
            + timedelta(
                days=settings.REFRESH_TOKEN_EXPIRE_DAYS
            )
        )

        try:
            # Store refresh token session
            session = Session(
                customer_id=user.customer_id,
                refresh_token=refresh_token,
                expires_at=expire_date
            )

            db.add(session)
            db.commit()
            db.refresh(session)

            logger.info(
                f"User logged in successfully: {user.email}"
            )

            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer",
                "user": {
                    "customer_id": str(
                        user.customer_id
                    ),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role
                }
            }

        except Exception as e:
            db.rollback()

            logger.error(
                f"Login failed: {str(e)}"
            )

            raise e

    def logout(
        self,
        db,
        refresh_token: str
    ):
        """
        Logout user by deleting session.
        """

        session = (
            db.query(Session)
            .filter(
                Session.refresh_token
                == refresh_token
            )
            .first()
        )

        if session:
            db.delete(session)
            db.commit()

            logger.info(
                "User logged out successfully."
            )

        return {
            "message":
            "Logout successful"
        }

    def refresh_access_token(
        self,
        db,
        refresh_token: str
    ):
        """
        Generate a new access token
        using refresh token.
        """

        session = (
            db.query(Session)
            .filter(
                Session.refresh_token
                == refresh_token
            )
            .first()
        )

        if not session:
            raise InvalidCredentials()

        user = (
            db.query(Customer)
            .filter(
                Customer.customer_id
                == session.customer_id
            )
            .first()
        )

        if not user:
            raise InvalidCredentials()

        new_access_token = (
            create_access_token(
                {
                    "sub": str(
                        user.customer_id
                    ),
                    "role": user.role
                }
            )
        )

        logger.info(
            f"Access token refreshed for {user.email}"
        )

        return {
            "access_token":
            new_access_token,
            "token_type":
            "bearer"
        }

        