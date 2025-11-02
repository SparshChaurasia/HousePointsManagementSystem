# House Points Management System

A comprehensive Python-based application for managing house points in educational institutions. This system allows administrators to track student participation, record event results, and generate detailed activity reports.

## Features

- **Role-based Access**: Separate interfaces for administrators and regular users
- **Student Management**: Add and manage student records with house assignments
- **Event Tracking**: Create and manage school events with detailed information
- **Participation Records**: Track student participation in various events
- **Results Management**: Record event results and automatically distribute house points
- **Activity Reporting**: Generate comprehensive reports on system usage and performance
- **House Point Tracking**: Monitor cumulative points for each house

## Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- Required Python packages (see [requirements.txt](requirements.txt))

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd HousePointsManagementSystem
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   - Start your MySQL server
   - Execute the database schema:
     ```bash
     mysql -u root -p < schema/CreateDatabaseQuery.sql
     ```

4. **Configure database access credentials**:
   - Create a `.env` file in the project root directory
   - Add your database credentials in the format:
     ```
     DB_USER=your_username
     DB_PASSWORD=your_password
     ```

5. **Create initial user**:
   - Add a user to the Users table with appropriate role (Admin/User)

## Usage

Run the application with:
```bash
python main.py
```

### Administrator Functions
- Add/remove students
- Create and manage events
- Record event participants and results
- Generate activity reports
- View detailed system statistics

### User Functions
- View house points standings
- Check student points
- Browse event details and participants

## Project Structure

```
HousePointsManagementSystem/
├── core/                 # Core functionality modules
│   ├── exceptions.py     # Custom exception classes
│   ├── login.py          # Authentication system
│   └── utils.py          # Utility functions
├── schema/               # Database schema files
│   └── CreateDatabaseQuery.sql
├── admin_interface.py    # Admin-specific interface
├── user_interface.py     # User-specific interface
├── main.py               # Main application entry point
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Technology Stack

- **Language**: Python 3
- **Database**: MySQL
- **Libraries**: 
  - mysql-connector-python for database connectivity
  - prettytable for formatted console output
  - python-dotenv for environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is proprietary and intended for educational institution use.

## Support

For issues and feature requests, please contact the development team.