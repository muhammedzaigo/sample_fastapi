# FastAPI User CRUD API

A simple and efficient FastAPI application for user management with full CRUD (Create, Read, Update, Delete) operations. This project demonstrates best practices for building RESTful APIs with FastAPI, SQLAlchemy, and Docker.

## Features

- ✅ Full CRUD operations for user management
- ✅ RESTful API design with proper HTTP status codes
- ✅ Data validation using Pydantic models
- ✅ SQLAlchemy ORM with SQLite database
- ✅ Docker containerization
- ✅ API documentation with Swagger UI
- ✅ Search functionality for users
- ✅ Pagination support
- ✅ Error handling and validation
- ✅ Health check endpoint

## Project Structure

\`\`\`
fastapi-user-crud/
├── main.py              # FastAPI application and API endpoints
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic models for request/response
├── crud.py              # Database operations
├── database.py          # Database configuration
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── .dockerignore       # Docker ignore file
├── .env.example        # Environment variables example
└── README.md           # Project documentation
\`\`\`

## API Endpoints

### Base Endpoints
- `GET /` - Welcome message
- `GET /health` - Health check

### User Management
- `POST /users/` - Create a new user
- `GET /users/` - Get all users (with pagination and search)
- `GET /users/{user_id}` - Get a specific user by ID
- `PUT /users/{user_id}` - Update a specific user
- `DELETE /users/{user_id}` - Delete a specific user
- `GET /users/stats/count` - Get total count of users

## Quick Start

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
   \`\`\`bash
   git clone <repository-url>
   cd fastapi-user-crud
   \`\`\`

2. **Build and run with Docker Compose**
   \`\`\`bash
   docker-compose up --build
   \`\`\`

3. **Access the API**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

### Option 2: Local Development

1. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. **Run the application**
   \`\`\`bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   \`\`\`

## API Usage Examples

### Create a User
\`\`\`bash
curl -X POST "http://localhost:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{
       "email": "john.doe@example.com",
       "first_name": "John",
       "last_name": "Doe",
       "password": "securepassword123",
       "is_active": true
     }'
\`\`\`

### Get All Users
\`\`\`bash
curl -X GET "http://localhost:8000/users/"
\`\`\`

### Get Users with Pagination and Search
\`\`\`bash
curl -X GET "http://localhost:8000/users/?skip=0&limit=10&search=john"
\`\`\`

### Get a Specific User
\`\`\`bash
curl -X GET "http://localhost:8000/users/1"
\`\`\`

### Update a User
\`\`\`bash
curl -X PUT "http://localhost:8000/users/1" \
     -H "Content-Type: application/json" \
     -d '{
       "first_name": "Jane",
       "email": "jane.doe@example.com"
     }'
\`\`\`

### Delete a User
\`\`\`bash
curl -X DELETE "http://localhost:8000/users/1"
\`\`\`

## Database Schema

### User Model
\`\`\`python
class User(Base):
    id: int (Primary Key)
    email: str (Unique, Required)
    first_name: str (Required)
    last_name: str (Required)
    hashed_password: str (Required)
    is_active: bool (Default: True)
    created_at: datetime (Auto-generated)
    updated_at: datetime (Auto-updated)
\`\`\`

## Environment Variables

Copy `.env.example` to `.env` and configure:

\`\`\`env
DATABASE_URL=sqlite:///./users.db
API_HOST=0.0.0.0
API_PORT=8000
\`\`\`

## Docker Commands

### Build the image
\`\`\`bash
docker build -t fastapi-user-crud .
\`\`\`

### Run the container
\`\`\`bash
docker run -p 8000:8000 fastapi-user-crud
\`\`\`

### Using Docker Compose
\`\`\`bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
\`\`\`

## Development

### Adding New Features
1. Update models in `models.py`
2. Create/update Pydantic schemas in `schemas.py`
3. Add database operations in `crud.py`
4. Create API endpoints in `main.py`

### Database Migrations
For production use, consider using Alembic for database migrations:
\`\`\`bash
pip install alembic
alembic init alembic
\`\`\`

## Production Considerations

1. **Security**
   - Use proper password hashing (bcrypt, scrypt)
   - Implement JWT authentication
   - Add rate limiting
   - Use HTTPS

2. **Database**
   - Switch to PostgreSQL for production
   - Implement connection pooling
   - Add database migrations

3. **Monitoring**
   - Add logging
   - Implement metrics collection
   - Set up health checks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License.
