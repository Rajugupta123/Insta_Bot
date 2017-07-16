import requests
from termcolor import colored
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

APP_ACCESS_TOKEN = '5701511646.03769e4.319c574f15bd438bb53cc218c7ef38c4'  #Global variable for App Access Token
BASE_URL = 'https://api.instagram.com/v1/'                                #Global Variable for Base URL

username='bnkk783'

#Function Declaration for proper Authentication
print colored('\n\t\t\t\tSandbox Users are: bnkk783\n','magenta',attrs=['bold'])
def password():
    while True:
        k = raw_input('Enter password:')
        if k == 'raju123':
            print'\tWelcome to InstaBot'
            break
        elif k != 'raju123':
            print'\tWrong Password, try again!'
password()

#Function for getting Self Information

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    self_info = requests.get(request_url).json()
    if self_info['meta']['code'] == 200:
        if len(self_info['data']):
            print'ID is %s'%(self_info['data']['id'])
            print 'Username: %s' % (self_info['data']['username'])
            print 'No. of followers: %s' % (self_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (self_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (self_info['data']['counts']['media'])
            return (self_info['data']['id'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'



#Function declaration to get the ID of a user by username

def get_user_id(username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


#Function declaration to get the info of a user by username

def get_user_info(username):
    user_id = get_user_id(username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print'\t'
            print' ID is %s'%(user_info['data']['id'])
            print 'Username is: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'


#Function declaration to get your recent post

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)

    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your post has been downloaded!'
            #return own_media(['data']['id'])
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


#Function declaration to get the recent post of a user by username


def get_user_post(username):
    user_id = get_user_id(username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
            #print'ID is %s'%(user_media['data']['id'])
            #return user_media['data']['id']
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


#Function declaration to get the ID of the recent post of a user by username


def get_post_id(username):
    user_id = get_user_id(username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


#Function declaration to like the recent post of a user


def like_a_post(username):
    media_id = get_post_id(username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}

    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

#Function declaration to make a comment on the recent post of the user

def post_a_comment(username):
    media_id = get_post_id(username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)

    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

#Function declaration to make delete negative comments from the recent post

def delete_negative_comment(username):
    media_id = get_post_id(username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)

    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):                   #Condition check for Negative Comments
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'

def menu():
    while True:
        print'MENU:-\n'

        print"1.Get your own details"
        print "2.Get details of a user by username"
        print "3.Get your own recent post"
        print "4.Get the recent post of a user by username"
        print "5.Like the recent post of a user"
        print "6.Make a comment on the recent post of a user"
        print "7.Delete negative comments from the recent post of a user"
        print "8.Exit"

        input=int(raw_input('Enter a choice:(1-8):'))
        if input==1:
            self_info()
        elif input==2:
            username=raw_input('Enter username of Sandbox user:')
            get_user_info(username)
        elif input==3:
            get_own_post()
        elif input==4:
            username=raw_input('Enter username')
            get_user_post(username)

        elif input==5:
            username = raw_input("Enter the username of the user: ")
            like_a_post(username)
        elif input == 6:
            username = raw_input("Enter the username of the user: ")
            post_a_comment(username)
        elif input == 7:
            username = raw_input("Enter the username of the user: ")
            delete_negative_comment(username)
        elif input == 8:
            print'Thanks For Using Instabot'
            exit()
        else:
            print "wrong choice"
menu()





