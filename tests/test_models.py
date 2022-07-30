from test_data import User, Following, Mypage, Post, Comment, Like


def test_new_user():
    user = User('pearlyn', 'testtest', 'Pearl', 'Jones', 'flairpearllee@gmail.com', '123123123', 'https://github.com/pearlilyy/postalk')
    assert user.username == 'pearlyn'
    assert user.password == 'testtest'
    assert user.first_name == 'Pearl'
    assert user.last_name == 'Jones'
    assert user.email == 'flairpearllee@gmail.com'
    assert user.phone == '123123123'
    assert user.picture == 'https://github.com/pearlilyy/postalk'

def test_new_following():
    following = Following(1, 2)
    assert following.user_id == 1
    assert following.following_id == 2

def test_new_mypage():
    mypage = Mypage(2, 'Hihi')
    assert mypage.user_id == 2
    assert mypage.introduction == 'Hihi'

def test_new_post():
    post = Post(1, 'I am testing my codes.', 'http', 'LA')

    assert post.user_id == 1
    assert post.note == 'I am testing my codes.'
    assert post.photo == 'http'
    assert post.location == 'LA'

def test_new_comment():
    comment = Comment('testing is not fun..', 1, 2)

    assert comment.content == 'testing is not fun..'
    assert comment.commenter_id == 1
    assert comment.post_id == 2


def test_new_like():
    like = Like(5, 7)

    assert like.user_id == 5
    assert like.post_id == 7