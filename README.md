# GlobeTrotter
Hotel and Flight booking web application

System architecture: 
The system is intended to handle information on flights, lodging, and rooms that are offered in a certain city. The user can choose to register or log in on the index page, but they can also finish their transaction without doing either. The input areas on the homepage allow users to enter the dates of their trip, check-in, and checkout. Users are given a list of hotels depending on the destination they have specified, and they are able to choose from these possibilities by looking at factors like price, guest rating, and availability for the dates of check-in and check-out, they can also use the tools on this page to sort the results according to price with the help of a mergesort algorithm. After making their pick, users are shown a list of rooms with information on each one, including the type of accommodation, price, amenities, kind of bed, and size. The user will then be able to reserve a room, submit payment information, and get a BookingID that will allow them to view details of any reservations they have made in the past or present.

Similar to this, the consumer may access a search bar by clicking on the "Flights" tab, where they can enter information such the departure and arrival dates, as well as the city of departure and arrival. After that, a selection of flights from various airlines will be shown to them along with their respective costs. They will receive a second BookingID after completing their booking, which they can use to access their flight reservations on the 'My Bookings' tab. Additionally, users can log in to the portal to change any details related to reservations they already have. By selecting the "Site Analytics" tab, site administrators may access business insights such as the number of users who have registered, logged in, and completed bookings each month, as well as the availability and booking status of hotels. This information helps them make informed decisions.


Modular Design: Hotel Booking Workflow
<img width="444" alt="image" src="https://github.com/user-attachments/assets/a1f100a2-aeb0-45f6-8088-23f8df2f8fa7">

Flight Booking Workflow
<img width="650" alt="image" src="https://github.com/user-attachments/assets/00f5305c-685a-4192-982a-06e6a6a1efe6">

Naviagtion Workflow
<img width="650" alt="image" src="https://github.com/user-attachments/assets/574d2688-f42c-4f35-a7ad-291431c9fc89">

OOP: Concept Of Inheritance --> The following tables display inheritance amongst the functions in the hotel options, hotel booking and flight booking modules.
<img width="562" alt="image" src="https://github.com/user-attachments/assets/074aaabf-f86b-40ee-9ba5-3acb3194fc61">
<img width="562" alt="image" src="https://github.com/user-attachments/assets/a185d079-4107-4032-9119-390622fb9791">
<img width="562" height="300" alt="image" src="https://github.com/user-attachments/assets/dbe75fcf-e155-4678-a7a0-55510c6ca400">
<img width="562" height="300" alt="image" src="https://github.com/user-attachments/assets/f1d8f937-27ad-4b00-bf7e-9c67d6dcb6bc">

Database Design - ERD
The following tables have been normalised in 1 - to - many relationships.
● On the payment form when a user is going to submit their details such as: fullname, email, address, card number etc, their data will be stored in app_booking and app_udetails table that are connected in a 1-to-many relationship, therefore one user can have many bookings.

● Cancellation will delete the same booking and user details from app_booking and app_udetails table, therefore both tables have booking_id as a foreign key.

<img width="562" alt="image" src="https://github.com/user-attachments/assets/20843ff9-e46b-4d54-aad0-5c405595bd9e">

● The table app_hotel_details stores details such as - name, location etc about different hotels.

● The table app_room_d will have a 1-to-many relationship with app_hotel_details as it stores the different rooms found in each hotel.

● The table app_extra will store meals and parking charges for every hotel in the app_hotel_details table.

<img width="562" alt="image" src="https://github.com/user-attachments/assets/cc19ef89-ba3b-4619-a772-15c62d773cfe">

● In the table app_flightudetails, one user can have many bookings and each booking will be unique for every user.

<img width="562" alt="image" src="https://github.com/user-attachments/assets/76d99b20-0835-4200-b42d-15c2d073a9be">


https://github.com/user-attachments/assets/ae91507f-8fd1-4db7-93da-0d38831ce3cb






https://github.com/user-attachments/assets/7367cf6b-cdec-44c1-8e15-053231a51730












