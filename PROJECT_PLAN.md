# HomeFix – Project Plan

## 1. Project Overview

HomeFix is a fictional general home maintenance company. This project will demonstrate a professional business website and a service-request management system built with Django.

The main objective is to deliver a functional MVP that supports customer service requests and administrative job management.

## 2. Target Users

**Customers**
- Browse maintenance services.
- View service information.
- Submit maintenance requests.
- Provide property and contact details.

**Administrators**
- Manage maintenance services.
- Review incoming requests.
- Contact customers.
- Update request statuses.
- Track job progress.

## 3. Core Services

- General household repairs
- Furniture assembly
- Painting and minor improvements
- Door, cabinet, and fixture repairs
- Home installations
- Basic property maintenance

## 4. MVP Features

### Public Website
- Home
- About
- Services
- Service Details
- Request a Service
- Contact
- Privacy Policy

### Service Request System

The request form will collect:
- Customer name
- Email
- Phone number
- Requested service
- Preferred date
- Preferred time
- Property address
- Property type
- Optional description
- Privacy consent

Validation requirements:
- Required field validation
- Valid email and phone input
- Reject past requested dates
- Basic duplicate and spam protection
- Clear success and error messages

Requests remain unconfirmed until reviewed by the company.

### Administrative Management

Administrators should be able to:
- View all service requests.
- Search and filter requests.
- View individual request details.
- Update request statuses.
- Add internal notes.
- Manage available services.

### Request Statuses

- Pending
- Reviewing
- Contacted
- Scheduled
- In Progress
- Completed
- Cancelled
- Declined

### Dashboard

Display basic operational information:
- Total requests
- Pending requests
- Scheduled jobs
- Completed jobs
- Recent requests

## 5. Technology

- Python
- Django
- Django Templates (DTL)
- HTML
- Tailwind CSS
- JavaScript
- Alpine.js where useful
- SQLite for local development
- PostgreSQL for production
- Git and GitHub

React is not part of this project.

## 6. Django Application Structure

Planned applications:

- `core` – public pages and shared website functionality.
- `services` – maintenance service management.
- `bookings` – customer requests and job management.
- `config` – Django project configuration.

## 7. Development Roadmap

### Milestone 1 – Project Setup
- Create Django project.
- Configure applications.
- Configure development environment.
- Set up Git and GitHub.
- Prepare project documentation.

### Milestone 2 – Website Design
- Define the design system.
- Build shared navigation and footer.
- Create responsive public page layouts.
- Implement the homepage.

### Milestone 3 – Service Management
- Create service models.
- Add service management.
- Display services dynamically.
- Create service detail pages.

### Milestone 4 – Service Request System
- Create request model.
- Build request form.
- Add validation.
- Save requests.
- Display confirmation messages.

### Milestone 5 – Request Administration
- View and manage requests.
- Search and filter requests.
- Update statuses.
- Add internal notes.

### Milestone 6 – Management Dashboard
- Display key operational metrics.
- Show recent requests.
- Improve management usability.

### Milestone 7 – Testing and Security
- Test forms and models.
- Test administrative workflows.
- Validate permissions.
- Review security and error handling.
- Test responsive layouts.

### Milestone 8 – Deployment
- Prepare production settings.
- Configure PostgreSQL.
- Deploy the application.
- Document setup and deployment.

### Milestone 9 – Portfolio Presentation
- Improve README and screenshots.
- Prepare a project demonstration video.
- Add the project to the developer portfolio.
- Prepare an accurate project description for GitHub and professional profiles.

## 8. Out of Scope for the First MVP

To keep the first version manageable, we will not implement:

- Online payments
- Subscription billing
- Multi-tenancy
- Customer accounts
- WhatsApp or SMS integrations
- GPS and route optimization
- Employee payroll
- Complex staff scheduling
- Mobile applications
- Advanced analytics

## 9. Development Principles

- Build one milestone at a time.
- Keep the architecture simple and consistent.
- Prioritize working features over unnecessary complexity.
- Test each major feature before moving forward.
- Avoid duplicating working functionality.
- Keep the project suitable for a beginner-to-intermediate Django developer's portfolio.
