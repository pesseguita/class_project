from post import Post
from user import User

if __name__ == '__main__':
    app_user_one = User("paula@gmail.com", "Paula", "pwd", "engineer")
    print(app_user_one.get_user_info())
    app_user_one.change_password("outra")
    print(app_user_one.get_user_info())

    post = Post("on a mission", app_user_one.name).get_post_info()
    print(post)