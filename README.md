# AFIND Formation

**AFIND Formation** is a web-based platform designed to manage training sessions, enrollments, and site content while ensuring seamless administration and user-friendly interactions.

---

## ✨ Features

- **Dynamic Training Management**: Create, update, and manage training sessions with ease.
- **Enrollment System**: Handle enrollments, search, filter, and export data to CSV.
- **Site Content Management**: Control static content like FAQ, Privacy Policy, and Terms of Service directly from the admin panel.
- **Customizable Admin Panel**: Enhanced Django admin with inline forms, custom actions, and tailored permissions.
- **Contact Messages**: View and manage messages sent via the contact form.

---

## 🛠 Technologies Used

- **Backend**: Python, Django  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: SQLite/MySQL  
- **Admin Customization**: Django Admin  
- **Data Analysis**: Pandas (for CSV export/import)

---
## 🖥 Usage

### Application URLs

- **Home**: `/`  
- **About**: `/a-propos/`  
- **Trainings**: `/formations/`  
- **Training Details**: `/formation/<int:pk>`  
- **Contact**: `/contact/`  
- **FAQ**: `/faq/`  
- **Privacy Policy**: `/politique-de-confidentialite/`  
- **Terms of Service**: `/conditions-generales-d-utilisation/`  

### Admin Panel Features

1. **Training Management**:
   - Inline image uploads for each training.
   - Search and filter by title, department, and instructor.
   - Manage training sessions directly from the admin.

2. **Enrollment Management**:
   - View and edit enrollment details.
   - Search and filter by name, phone, formation, and specialty.
   - Export enrollments as CSV.

3. **Contact Messages**:
   - View messages from users with details like name, email, subject, and date.

4. **Site Content**:
   - Manage static pages like FAQ, Privacy Policy, and Terms of Service.
   - Restrict adding or deleting site content beyond predefined types.

5. **Site Settings**:
   - Manage configuration settings accessible only to superusers.

---

## 📬 Contact

- **Author**: Seyf Eddine Abdellaoui  
- **Email**: [seyfeddine.abdellaoui@gmail.com](mailto:seyfeddine.abdellaoui@gmail.com)  
- **GitHub Profile**: [seyf-eddine19](https://github.com/seyf-eddine19)
