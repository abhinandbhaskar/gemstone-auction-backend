# Online Gemstone Auction Platform - Backend Models

## Submitted By:
Name:AbhinandBhaskar
Submission Title:Auction Assessment

## Project Overview

This project outlines the backend data models for a online gemstone auction platform. Users can register and also they have ability to act like seller. after register they can buy or sell gemstones through time based actions. Features include gemstone listing,bidding,action clusure,payment tracting,moderation,group auctions and a watchlist system.



## Requirements Analysis & Exploration

** Key Features covered:

 - User registration,user type selection (user,admin),seller verification,profile info

 - Gemstone listing with certification and grading (clarity,carat) and also gemstone_type selection through previously added model GemstoneType

 - Group auctions (auction lots)

 - Time Based Bidding and automatic auction closure

 - Winning Bid assignment and payment tracting

 - Report system for moderation

 - Watchlist feature for auction tracking without bidding

#### Client-Oriented Questions Asked in the Review Meeting:

1.Should every user be able to both buy and sell gemstones, or are there separate user types (buyer vs seller)? 

2.Will sellers need to go through any verification process before they’re allowed to post gemstones for auction? 

3.Is the auction duration fixed (e.g., always 7 days), or does the seller decide the duration? 

4.What happens if no one places a bid — does the auction close without a sale or get extended?

5.Can users bid more than once on the same gemstone?


6.How will users be notified if they are outbid — via email, SMS, or in-app notification?

7.	What payment methods do you plan to support (bank, card, crypto)?

8.Should we store actual transaction details, or just a payment status flag?

9.Can users report any listing, or only if they are involved in the transaction?

10.	What are the moderation actions available to admins — delete listing, suspend user, etc.?

## Strategic Planning

### Scaling Approach:

** How I Plan to Scale This Project in the Future **

 - The project is built in separate modules, so it will be easier to add new features like SMS alerts, email updates, or even support auctions for other items (like artwork, collectibles, etc.).

 - The UserProfile model makes it flexible to introduce new roles in the future, like moderators or premium sellers.

 - For time-based tasks like closing auctions or sending reminders, I plan to use background jobs with tools like Celery or cron in a real project.

 - I also plan to add pagination to auction listings, gemstone views, and bid histories. This will make the site faster and more responsive when there are a lot of users or data.

 ** Features I Can Add Later **

 -  Blockchain certification to make gemstone authenticity more secure.

 - if possible i will try to add AI features like automatic gemstone grading or checking for fake listings using uploaded images.

 ## Risks & My Solutions

____________________________________________________________________________________
What Could Go Wrong             |    How I Plan to Handle It
____________________________________________________________________________________
* Fake gemstone listings        |  * Sellers will need to upload certificates, and users can report issues.

* Spamming bids or cheating     |  * I will add rules to stop self-bidding and limit how fast people can place bids.

* Auctions not closing on time	|  * try to Docker-like tool or setup that gives live updates instead signals

* Payment errors	            |  * Track payment status and show errors clearly so users can retry or get help.

* Site getting slow             |  * Use pagination,database indexing and maybe caching later if traffic grows a lot.
 with lots of users	
 _____________________________________________________________________________________




## Project Modules

1.User & Profile
For user accounts, profile info, and checking if someone is allowed to sell.

2.Gemstone Listings
Sellers can list gemstones with all details like name, carat, clarity, and certification.

3.Auction & Auction Lot
Group multiple gemstones into a single auction lot and run time-based auctions.

4.Bidding System
Buyers can place bids. The system keeps track of the highest bid.

5.Payment
After winning, buyers can pay through Razorpay. Payment info is saved securely.

6.Reports
Users can report fake or problematic listings. Moderators can check and act on them.

7.Watchlist
Users can keep an eye on auctions without bidding immediately.

## Why I Designed It Like This
 - Each part is separated to make the code easier to understand and update later.

 - If I want to add new features in the future, I won’t need to change everything.

 - Frontend and backend can be developed in parallel because of clear modules.

# My Development Plan (As a Solo Developer)
_____________________________________________________________
Step    |  What i Did                             |  Time Taken
_____________________________________________________________

Step 1  | Understand the features plan the models   | 1 day

step 2  | Create the models and link them correctly | 2 days
 
Step 3	| Test the models and fix small issues      | 1 day

step 4  | Write this README and finalize the project | 0.5 day

Extra Time	| For client changes or bugs             | 1 day

Extra time may vary based on complexity of task or easy i can do within 0.5 days or very faster


Total Time	| About 5.5 or 6 days
_____________________________________________________________

## What I Learned / What I’d Do Differently
 - In a real job, I would start by asking more questions and getting clear requirements with the team.

 - I’d use diagrams(DFD or Lucid Chart) to show how all the models connect so it's easier for others to understand.

 - If the project becomes big, I’d break it into smaller services, like separate apps for users, auctions, and payments.

 - In a team, I would follow proper version control, review others' code, and work using clear communication with designers and frontend developers.


## Files I’m Submitting
models.py – Django models for the whole project.

README.md – This file with my planning and explanation.

## GitHub Repo Link
-  GitHub repo

    https://github.com/abhinandbhaskar/gemstone-auction-backend.git




