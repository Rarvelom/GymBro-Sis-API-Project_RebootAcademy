# GymBro-Sis-API-Project_RebootAcademy

# 🏋️‍♀️ GymBro/Sis – Find Your Workout Partner API

**GymBro/Sis** is a fitness-focused RESTful API and user interface designed to help people find compatible training partners based on goals, experience level, schedule, and location. Built with **FastAPI**, **MongoDB**, and **Streamlit**, this project promotes health, community, and consistency in fitness routines.

---

## 🚀 Tech Stack

- **Backend:** FastAPI
- **Database:** MongoDB (NoSQL)
- **Frontend:** Streamlit
- **Deployment-ready:** Lightweight and modular

---

## 📦 Features

- Create and manage **user profiles** (age, weight, experience, availability)
- Define and explore **training spots** (gyms, parks, home)
- Organize and join **training sessions** by type and level
- Match with others based on shared availability and training preferences
- Simple and intuitive **Streamlit interface**

---

## 🧱 Database Structure
```text
┌───────────────────┐       ┌───────────────────┐       ┌───────────────────┐
│      users        │       │      spots        │       │    trainings       │
├───────────────────┤       ├───────────────────┤       ├───────────────────┤
│ _id: ObjectId     │───────│ _id: ObjectId     │◄──────│ _id: ObjectId     │
│ name: String      │       │ user_id: ObjectId │       │ user_id: ObjectId │
│ weight: Float     │       │ name: String      │       │ spot_id: ObjectId │
│ experience: String│       │ address: String   │       │ type: String      │
│ age: Int          │       │ schedule: String  │       │ level: String     │
│ availability:     │       │ type: String      │       │ datetime: String  │
│       [String]    │       └───────────────────┘       └───────────────────┘
│ description: String│
└───────────────────┘
```


📅 Timeline

   Day 1: Backend (FastAPI + MongoDB + API endpoints)

   Day 2: Frontend (Streamlit + API integration + Matching logic)

👥 Team & Roles

  Javier Barroso – Backend developer & database structure

  Laura Suárez – Frontend development & UX

  Ricardo – API design & integration logic

Working in Mob Programming format to ensure collaboration and shared ownership across all parts of the code.

🧠 Inspiration

“Training alone builds discipline. Training together builds community.”
This app aims to create a stronger, healthier fitness culture – one workout partner at a time.

📝 License

MIT License – Free to use and extend with proper credit.
