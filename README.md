# My Personal Blog

Welcome to My Personal Blog project! This project implements a blogging platform using FastAPI and SQLAlchemy, where users can create posts, organize them into categories, add tags, and leave comments.

## Features

- **User Management**: Create user accounts with secure authentication.
- **Post Management**: Create, read, update, and delete blog posts.
- **Category Organization**: Categorize posts into different categories.
- **Tagging**: Associate tags with posts for better organization and searchability.
- **Comment System**: Allow users to comment on posts.

## Technologies Used

- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- SQLite (or your chosen database engine): Lightweight database for storing blog data.
- Pydantic: Data validation and settings management using Python type annotations.
- JWT (JSON Web Tokens): For secure user authentication and authorization.

## Setup

### Prerequisites

- Python 3.10+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abduvalimurodullayev1/my_personal_blog.git
    cd my_personal_blog
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

### User Endpoints

- **Create User**: `POST /users`
    - Request body: `{"email": "user@example.com", "name": "John Doe", "password": "yourpassword"}`
    - Response: User details including `id`, `email`, `name`, and `date_created`.

- **Login User**: `POST /login`
    - Request body: `{"email": "user@example.com", "password": "yourpassword"}`
    - Response: JWT token for authentication.

### Post Endpoints

- **Create Post**: `POST /posts`
    - Request body: `{"title": "Post Title", "content": "Post Content", "category_id": 1, "tags": [1, 2]}`
    - Response: Created post details including `id`, `title`, `content`, `date_created`, `author`, `category`, and `tags`.

- **Get All Posts**: `GET /posts`
    - Response: List of all posts with details.

- **Get Post by ID**: `GET /posts/{post_id}`
    - Path parameter: `post_id` (ID of the post)
    - Response: Details of the post with specified `post_id`.

- **Update Post**: `PUT /posts/{post_id}`
    - Path parameter: `post_id` (ID of the post)
    - Request body: Updated post data (`title` and/or `content`)
    - Response: Updated post details.

- **Delete Post**: `DELETE /posts/{post_id}`
    - Path parameter: `post_id` (ID of the post)
    - Response: Message confirming deletion.

### Category Endpoints

- **Create Category**: `POST /categories`
    - Request body: `{"name": "Category Name"}`
    - Response: Created category details including `id` and `name`.

- **Get All Categories**: `GET /categories`
    - Response: List of all categories with details.

### Comment Endpoints

- **Create Comment**: `POST /comments`
    - Request body: `{"content": "Comment Content", "post_id": 1}`
    - Response: Created comment details including `id`, `content`, `date_created`, `user`, and `post`.

- **Get Comments for Post**: `GET /posts/{post_id}/comments`
    - Path parameter: `post_id` (ID of the post)
    - Response: List of comments associated with the specified post.

## Project Structure

- **main.py**: Main application file with FastAPI routes and startup configurations.
- **models.py**: SQLAlchemy models defining database tables (`User`, `Post`, `Category`, `Comment`, `Tag`, etc.).
- **schemas.py**: Pydantic schemas for data validation and serialization.
- **database.py**: Database configuration and connection setup using SQLAlchemy.
- **requirements.txt**: List of Python dependencies.

## Running Tests

To run tests, ensure you have `pytest` installed:
```bash
pytest
