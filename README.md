# Procure_
# Procure Pro Integration

This project demonstrates an integration with the Procore platform to fetch project data and handle webhook notifications for project creation, updates, and deletions.

## Features
1. **Webhook Integration**: Receives notifications from Procore for project changes.
2. **Project Management**: Stores project details in a database (SQLite) for retrieval and updates.
3. **Secure APIs**: Implements error handling and secure endpoints for Procore interactions.

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.2
- Procore Developer Sandbox account
- SQLite or PostgreSQL database
  
The purpose of this project is to build a basic integration with Procore, a construction management platform, to track changes in project data, such as the creation, update, or deletion of projects. The integration should:

Register for notifications from Procore about project data changes (webhooks).
Import existing project data from Procore for a given company ID and store the details in a Postgres SQL database.
Process incoming notifications (e.g., new, updated, or deleted projects) from Procore and store them in your database.
The project also focuses on creating a secure, well-structured API with robust error-handling and hosting it on a platform (e.g., Render.com) for Procore to call. The goal is to automate data flow between Procore and your system, ensuring that updates to project data on Procore are reflected in your database automatically.
