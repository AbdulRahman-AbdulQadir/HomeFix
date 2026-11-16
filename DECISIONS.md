# HomeFix – Architecture and Design Decisions

## 1. Business Identity

### Brand Name
HomeFix

### Business Model
General Home Maintenance.

### Brand Direction
Professional, reliable, welcoming, and trustworthy.

### Project Purpose
HomeFix is a fictional home maintenance company created as a self-initiated portfolio project. It demonstrates a practical business website and service-request management system.

The project must not be presented as a real operating company or client project.

## 2. UI/UX Design

### Brand Direction
Balanced Green – professional, fresh, and trustworthy.

### Color Palette
- Forest Green: `#14532D`
- Primary Green: `#15803D`
- Light Green: `#86EFAC`
- Background: `#F8FAF9`
- Main Text: `#17211B`
- Secondary Text: `#647067`
- Borders: `#E5EAE6`

### Typography
Inter or a similar modern sans-serif font.

### Frontend Technologies
- Django Templates (DTL)
- Tailwind CSS
- JavaScript
- Alpine.js when necessary

### Design Principles
- Mobile-first responsive design.
- Consistent spacing and typography.
- Reusable components.
- Accessible colors and controls.
- Clear service-request calls to action.
- Simple customer navigation.
- Professional home maintenance photography.
- Avoid unnecessary animations.
- Maintain a consistent design across all pages.

## 3. Homepage Structure

The homepage will contain:

1. Navigation
2. Hero section
3. Services overview
4. Why Choose HomeFix
5. How It Works
6. Service Areas
7. Testimonials (only clearly identified demo content)
8. Service Request CTA
9. Footer

## 4. Business Services

HomeFix represents a general home maintenance business.

Planned service categories include:
- General household repairs.
- Furniture assembly.
- Painting and minor improvements.
- Door, cabinet, and fixture repairs.
- Home installations.
- Basic property maintenance.

Specialized plumbing and electrical work must only be represented as services performed by appropriately qualified professionals.

## 5. Service Request and Appointment Rules

- Customers can submit service requests through the website.
- Submitting a request does not automatically confirm an appointment.
- Administrators must review incoming requests.
- The company contacts customers to discuss the request.
- Appointment dates and times are agreed upon separately.
- Request statuses must clearly communicate progress.
- Customers must receive a clear confirmation that their request was submitted, not that their appointment was booked.

## 6. Architecture Decisions

### Backend
- Python
- Django

### Frontend
- Django Templates (DTL)
- HTML
- Tailwind CSS
- JavaScript
- Alpine.js when necessary

### Database
- SQLite during development.
- PostgreSQL for production.

### Django Applications
- `core` – public website and shared functionality.
- `services` – maintenance service management.
- `bookings` – customer service requests and job management.
- `config` – Django project configuration.

### Architecture Principles
- Use Django's built-in features whenever practical.
- Keep the architecture simple and maintainable.
- Avoid unnecessary dependencies.
- Reuse templates and components.
- Keep business logic organized within the appropriate applications.
- Do not introduce React.

## 7. MVP Development Principles

- Prioritize a working MVP over unnecessary features.
- Develop one milestone at a time.
- Test important functionality before moving forward.
- Use Django Admin initially where it saves development time.
- Avoid implementing online payments in the first MVP.
- Do not build complex features before they are needed.
- Keep the project suitable for a beginner-to-intermediate Django developer portfolio.

## 8. Portfolio and Presentation Rules

- Present HomeFix honestly as a self-initiated demonstration project.
- Do not claim that it was developed for a real client.
- Do not present fictional testimonials as genuine customer reviews.
- Use realistic demonstration data where needed.
- Keep the GitHub repository and project documentation consistent with the HomeFix identity.
