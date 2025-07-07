# Fantasy Soccer App Backend

A comprehensive fantasy soccer application backend built with FastAPI, PostgreSQL, and SQLAlchemy. This application supports English Premier League (EPL) fantasy soccer with plans for expansion to other leagues.

## Features

- **User Management**: Registration, authentication, and user profiles
- **League Management**: Create and join fantasy leagues with invite codes
- **Team Management**: Build and manage fantasy teams
- **Player Data**: Comprehensive EPL player database
- **Draft System**: Snake draft functionality for team building
- **Trading System**: Player trades between teams
- **Match Tracking**: Real match data and player performance tracking
- **JWT Authentication**: Secure API access with JWT tokens

## Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (AWS RDS)
- **ORM**: SQLAlchemy
- **Authentication**: JWT with python-jose
- **Password Hashing**: bcrypt with passlib
- **Data Validation**: Pydantic
- **Server**: AWS EC2 (Ubuntu)

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL database
- AWS EC2 instance (for production)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FantasyFoot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   DB_HOST=your-db-host
   DB_PORT=5432
   DB_NAME=your-db-name
   DB_USER=your-db-user
   DB_PASSWORD=your-db-password
   SECRET_KEY=your-secret-key-here
   ```

4. **Initialize the database**
   ```bash
   python scripts/init_db.py
   ```

5. **Import EPL data**
   ```bash
   python scripts/import_data.py
   ```

6. **Run the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API docs**: http://localhost:8000/docs
- **ReDoc documentation**: http://localhost:8000/redoc

### Authentication

The API uses JWT authentication. To access protected endpoints:

1. **Register a user**:
   ```bash
   POST /auth/register
   {
     "username": "your_username",
     "email": "your_email@example.com",
     "password": "your_password"
   }
   ```

2. **Login to get access token**:
   ```bash
   POST /auth/login
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

3. **Use the token in subsequent requests**:
   ```bash
   Authorization: Bearer <your_access_token>
   ```

### Key Endpoints

#### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get access token
- `GET /auth/me` - Get current user info

#### Leagues
- `POST /leagues/` - Create new league
- `GET /leagues/` - Get user's leagues
- `GET /leagues/{league_id}` - Get league details
- `POST /leagues/{league_id}/join` - Join league with invite code
- `PUT /leagues/{league_id}` - Update league (admin only)

#### Teams
- `GET /teams/` - Get user's teams
- `GET /teams/{team_id}` - Get team details
- `PUT /teams/{team_id}` - Update team
- `GET /teams/league/{league_id}` - Get all teams in league

#### Players
- `GET /footballers/` - Get players with filters
- `GET /footballers/{footballer_id}` - Get player details
- `GET /footballers/league/{league_name}` - Get players by league
- `GET /footballers/club/{club_id}` - Get players by club

#### Clubs
- `GET /clubs/` - Get clubs with filters
- `GET /clubs/{club_id}` - Get club details
- `GET /clubs/league/{league_name}` - Get clubs by league

## Database Schema

### Core Tables
- **users**: User accounts and authentication
- **leagues**: Fantasy leagues
- **teams**: User fantasy teams
- **clubs**: Real football clubs
- **footballers**: Real football players
- **fantasy_players**: Players selected by fantasy teams
- **matches**: Real match data
- **player_performances**: Individual player match statistics
- **trades**: Player trades between teams
- **drafts**: League draft sessions
- **draft_picks**: Individual draft selections

## Development

### Project Structure
```
FantasyFoot/
├── app/
│   ├── api/           # API routers
│   ├── auth/          # Authentication utilities
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic schemas
│   └── main.py        # FastAPI application
├── scripts/           # Utility scripts
├── data/              # Data files
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### Database Migrations
The application currently uses SQLAlchemy's `create_all()` for table creation. For production, consider using Alembic for migrations:

```bash
# Initialize Alembic
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

## Production Deployment

### AWS EC2 Setup
1. Launch Ubuntu EC2 instance
2. Install Python, PostgreSQL client, and other dependencies
3. Clone repository and install Python dependencies
4. Set up environment variables
5. Use systemd or supervisor to run the application
6. Set up reverse proxy (nginx) for SSL termination

### Security Considerations
- Use strong SECRET_KEY in production
- Enable HTTPS with SSL certificates
- Restrict database access with security groups
- Use environment variables for sensitive data
- Implement rate limiting
- Set up proper CORS origins

## Future Enhancements

- **Multiple Leagues**: Support for Champions League, World Cup, etc.
- **Real-time Updates**: WebSocket integration for live updates
- **Advanced Statistics**: More detailed player performance metrics
- **Mobile API**: Optimized endpoints for mobile applications
- **Admin Panel**: Web interface for league administration
- **Notifications**: Email/SMS notifications for important events
- **Data Sync**: Automated sync with external football APIs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue on the GitHub repository. 