# postalk

- Title
    Postalk. A sort of SNS which is based on posting.

- Description
    It's vary similar with Twitter or Instagram. Postalk is a platform to show one's opinion or thought. We can follow anyone whose contents we want to see. We can hit the like button on which we like.

- How did the project's design evolve over time?
    My table design was more simple when I first made it. But I divided some tables and linked them with Foreign Key. It will help database management more efficient.

- Did you choose to use an ORM or raw SQL? Why?
    I chose the raw SQL first, but changed to ORM. While using ORM, I learned more and understood better, which I wanted to do.

- What future improvements are in store, if any?
    I wanna make the data visualization when I understand it better. Also, I can add indexing to the database to make the speed higher in the future. But, I don't have enough data atm, I'll add it later.


- API Reference Table of endpoint paths, methods, parameters

|       endpoint     |   methods   |   parameters  |
| ------------------ | ----------- | ------------- |
| users_show         | GET         |               |
| users_create       | POST        |               |
| users_update       | PUT/PATCH   |               |
| users_delete       | DELETE      |               |
| posts_show         | GET         |               |
| posts_create       | POST        |               |
| posts_update       | PUT/PATCH   |               |
| posts_delete       | DELETE      |               |
| mypages_show       | GET         |               |
| mypages_create     | POST        |               |
| mypages_update     | PUT/PATCH   |               |
| mypages_delete     | DELETE      |               |
| likes_show         | GET         |               |
| likes_create       | POST        |               |
| likes_delete       | DELETE      |               |
| followings_show    | GET         |               |
| followings_create  | POST        |               |
| followings_delete  | DELETE      |               |
| comments_show      | GET         |               |
| comments_create    | POST        |               |
| comments_update    | PUT/PATCH   |               |
| comments_delete    | DELETE      |               |