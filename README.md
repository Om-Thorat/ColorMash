# ColorMash 🎨
![visitors](https://visitor-badge.glitch.me/badge?page_id=Om-Thorat.ColorMash&left_color=green&right_color=red)


## Remember Facemash? from [The Social Network](https://www.rottentomatoes.com/m/the-social-network). 💻

### That's it but just for ColorCombos. 🖌️
### Using an elo ♟️ rating system to rank colorcombos as voted by users.

## Deployment 🧑‍💻

To deploy this project locally

```bash
git clone https://github.com/Om-Thorat/ColorMash.git
```
Make sure you have Django installed
```bash
py -m django --version
```
Else install Django
```bash
pip install django
```
Enter the directory
```bash
cd ColorMash
```
Migrate to create the databases
```bash
py manage.py migrate
```
Run the server on a desired port
```bash
py manage.py runserver 3000
```
Now the page must be hosted on localhost:3000

Visit [localhost:3000/prettycombos](http://127.0.0.1:3000/prettycombos) To vote.

And [localhost:3000/prettycombos/leads](http://127.0.0.1:3000/prettycombos/leads) to see the Leaders.

The main page ie localhost:3000 is intended to be blank.

(Because i am too lazy to make a landing page.)

Thank You <3.
