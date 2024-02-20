# Django Channels Chat App

Welcome to the Django Channels Chat App, a real-time chat application built with Django and Django Channels. This application empowers users with the ability to join various chat rooms, send messages, and engage in real-time interactions.

## Features

- Multiple chat rooms
- Real-time message exchange using WebSockets
- User authentication (basic, extend as needed)
- Database storage for chat messages
- Simple and intuitive UI

## Getting Started

### Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python (3.8 or higher)
- Django
- Channels

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ChatApp.git
   cd ChatApp
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Visit the application in your web browser (default: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)).
2. Log in or create an account.
3. Explore available chat rooms and join a room.
4. Start sending and receiving messages in real-time.

## WebSocket Consumer

The WebSocket consumer, implemented in the `consumers.py` file, manages WebSocket connections, disconnections, and message exchanges among users in the same chat room.

## Database Models

The project utilizes Django models to represent chat rooms and messages. Find the models defined in the `models.py` file within the `ChatRoomApp` app.

## Views and Templates

The `views.py` file in the `ChatRoomApp` app contains views for rendering chat rooms and individual chat rooms. Corresponding templates are located in the `templates` folder.

## Django Settings

Project settings are specified in the `settings.py` file, encompassing special configurations for Django Channels, database settings, and other parameters.

## URL Configuration

The `urls.py` file configures URL pa
