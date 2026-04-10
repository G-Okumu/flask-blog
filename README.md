# Flask Blog

<p>This project is a Flask-based web application that allows users to manage a blog platform with profiles, blogs, and comments. The application leverages Flask for the backend framework, SQLAlchemy as the ORM for database interaction, and Marshmallow for serialization and deserialization of model instances. It also integrates with a MySQL database for storage and retrieval of data.</p>


## Key Features

- User management: Register users with profiles and password.
- Blog management: Create and list blog posts.
Comment system: Allow users to comment on blog posts.
- Serialization: JSON API for users, blogs, and comments via Marshmallow.


## Structure

<p>The project is organized as follows:</p>

- ```app.py```: The main application file that initializes the Flask app, database, and routes.
- ```models```: Contains database models for User, Blog, Profile, and Comment.
- ```schemas```: Contains Marshmallow schemas to serialize and deserialize model data.
- ```config.py```: Configuration settings for the app
- ```seed.py```: Script to seed the database with initial data for testing.


## Code Explanation

### Models

1. ``User`` - Represents a user in the application.
2. ``Profile`` - Represents the profile of a user
3. ``Blog`` - Represents a blog post.
4. ``Comment`` - Represents a comment made on a Blog

### Marshmallow Schemas

- Marshmallow is a Python library used for object serialization and deserialization. 
- It helps convert complex data types, such as database models or Python objects, into JSON format (serialization) and vice versa (deserialization).

- Marshmallow serves as a bridge between your Python objects (like SQLAlchemy models) and the data format (typically JSON) used in web requests and responses.

<p>These schemas are used to convert model instances to JSON format.</p>

###### How Does Marshmallow Improve Work in This Project?

- Marshmallow helps by converting database models (such as User, Blog, and Comment) into JSON, which is a standardized format for data exchange

###### Some of the Marshmellow terms used in the schema

- ``ma.SQLAlchemyAutoSchema`` - This is the base class provided by Marshmallow that automatically generates a schema for SQLAlchemy models. It uses the model to automatically create serialization logic based on the fields defined in the each model

- ``Class Meta`` - This inner Meta class provides metadata about the schema, such as the model it is associated with and other options.

- ``load_instance = True`` - Ensures that when Marshmallow deserializes data (i.e., converting JSON back into a Python object), it will return instances of the model (rather than just plain dictionaries).

- ``include_relationships = True`` - Tells Marshmallow to include relationships in the serialization

- ``model = ModelName `` - Specifies that this schema is for the model, meaning it will automatically handle the conversion of model objects


## Setup Instructions
### Requirements

<p>Before you begin, make sure you have the following installed:</p>

- Python 3.x
- MySQL Server
- pip3/pip for installing dependencies
- Virtual Environment

#### 1.  Clone the Repository

```
    ~ git clone this repo
    ~ cd flask-blog
```

#### 2.  Clone the Repository

- Setup virtual env

```
    ~ python3 -m venv yourvirtualenvname
    ~ source yourvirtualenvname/bin/activate
```

#### 3.  Install Dependencies

```
    ~ pip install -r requirements.txt
```

#### 4.  Configure Database

- In config.py, ensure that the S```QLALCHEMY_DATABASE_URI``` is configured with the correct MySQL database credentials.

#### 5. Run your Application

``~ Flask Run   ``

#### 6. Seed data

``~ python3 seed.py`` 





