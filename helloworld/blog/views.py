from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime

blog_entries = [
    {
        'id': 1,
        'title': 'Lorem, ipsum dolor.',
        'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi vitae corporis explicabo '
                'similique quam nisi laboriosam repellat dolor eligendi eius. Inventore!',
        'author_name': 'Lorem, ipsum.',
        'created_date': datetime(year=2020, month=9, day=20, hour=8, minute=13),
        'img_url': 'https://easyhonestfinancial.com/wp-content/uploads/2019/01/TECH.jpg',
        'comments': [
            {
                'author_name': 'Comment Author Name 1',
                'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=20, hour=8, minute=40),
            },
            {
                'author_name': 'Comment Author Name 2',
                'content': 'Lorem ipsum dolor sitt. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=20, hour=10, minute=12),
            },
            {
                'author_name': 'Comment Author Name 3',
                'content': 'Molestias qui doloribus eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=20, hour=14, minute=1),
            }
        ],
    },
    {
        'id': 2,
        'title': 'Lorem ipsum dolor sit.',
        'body': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiis perspiciatis nobis aliquid odit ea?'
                ' Consequatur obcaecati ab nostrum, mollitia fuga omnis architecto, dolores cumque quaerat '
                'similique earum vitae ipsa assumenda.',
        'author_name': 'Lorem.',
        'created_date': datetime(year=2020, month=9, day=18, hour=10, minute=21),
        'img_url': 'https://materializecss.com/images/sample-1.jpg',
        'comments': [
            {
                'author_name': 'Comment Author Name 1',
                'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=18, hour=12, minute=40),
            },
            {
                'author_name': 'Comment Author Name 2',
                'content': 'Lorem ipsum dolor sitt. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=18, hour=13, minute=12),
            },
            {
                'author_name': 'Comment Author Name 3',
                'content': 'Molestias qui doloribus eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=19, hour=14, minute=1),
            }
        ],
    },
    {
        'id': 3,
        'title': 'Lorem ipsum dolor sit.',
        'body': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiis perspiciatis nobis aliquid odit ea? Consequatur obcaecati ab nostrum, mollitia fuga omnis architecto, dolores cumque quaerat similique earum vitae ipsa assumenda.',
        'author_name': 'Lorem.',
        'created_date': datetime(year=2020, month=9, day=12, hour=12, minute=21),
        'img_url': 'https://coschedule.com/blog/wp-content/uploads/blog-post-templates.png',
        'comments': [
            {
                'author_name': 'Comment Author Name 1',
                'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=12, hour=12, minute=40),
            },
            {
                'author_name': 'Comment Author Name 2',
                'content': 'Lorem ipsum dolor sitt. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=12, hour=13, minute=12),
            },
            {
                'author_name': 'Comment Author Name 3',
                'content': 'Molestias qui doloribus eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=9, day=13, hour=14, minute=1),
            }
        ],
    },
    {
        'id': 4,
        'title': 'Lorem, ipsum dolor. OLD 1 ',
        'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi vitae corporis explicabo '
                'similique quam nisi laboriosam repellat dolor eligendi eius. Inventore!',
        'author_name': 'Lorem, ipsum.',
        'created_date': datetime(year=2020, month=8, day=20, hour=8, minute=13),
        'img_url': 'https://insights.bookbub.com/wp-content/uploads/2018/02/creative-blog-post-ideas-authors.png',
        'comments': [
            {
                'author_name': 'Comment Author Name 1',
                'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=20, hour=8, minute=40),
            },
            {
                'author_name': 'Comment Author Name 2',
                'content': 'Lorem ipsum dolor sitt. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=20, hour=10, minute=12),
            },
            {
                'author_name': 'Comment Author Name 3',
                'content': 'Molestias qui doloribus eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=20, hour=14, minute=1),
            }
        ],
    },
    {
        'id': 5,
        'title': 'Lorem ipsum dolor sit. OLD 2',
        'body': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiis perspiciatis nobis aliquid odit ea? Consequatur obcaecati ab nostrum, mollitia fuga omnis architecto, dolores cumque quaerat similique earum vitae ipsa assumenda.',
        'author_name': 'Lorem.',
        'created_date': datetime(year=2020, month=8, day=18, hour=10, minute=21),
        'img_url': 'https://www.ryrob.com/wp-content/uploads/2019/11/201-Best-Blog-Post-Ideas-Thatll-Drive-Traffic.jpg',
        'comments': [
            {
                'author_name': 'Comment Author Name 1',
                'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=18, hour=12, minute=40),
            },
            {
                'author_name': 'Comment Author Name 2',
                'content': 'Lorem ipsum dolor sitt. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=18, hour=13, minute=12),
            },
            {
                'author_name': 'Comment Author Name 3',
                'content': 'Molestias qui doloribus eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=19, hour=14, minute=1),
            }
        ],
    },
    {
        'id': 6,
        'title': 'Lorem ipsum dolor sit. OLD 3',
        'body': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiis perspiciatis nobis aliquid odit ea? Consequatur obcaecati ab nostrum, mollitia fuga omnis architecto, dolores cumque quaerat similique earum vitae ipsa assumenda.',
        'author_name': 'Lorem.',
        'created_date': datetime(year=2020, month=8, day=12, hour=12, minute=21),
        'img_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQxq-e9g45skAxqvopb4_qRGNHvm2nUNBJpCw&usqp=CAU',
        'comments': [
            {
                'author_name': 'Comment Author Name 1',
                'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=12, hour=12, minute=40),
            },
            {
                'author_name': 'Comment Author Name 2',
                'content': 'Lorem ipsum dolor sitt. Molestias qui doloribus '
                           'eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=12, hour=13, minute=12),
            },
            {
                'author_name': 'Comment Author Name 3',
                'content': 'Molestias qui doloribus eveniet, earum pariatur ipsa consequuntur ullam!',
                'created_date': datetime(year=2020, month=8, day=13, hour=14, minute=1),
            }
        ],
    }
]


def get_post_by_id(post_id):
    for post in blog_entries:
        if post['id'] == post_id:
            return post


def get_latest_posts():
    current_month = datetime.today().month
    return [post for post in blog_entries if post['created_date'].month == current_month]


def get_oldest_posts():
    current_month = datetime.today().month
    return [post for post in blog_entries if post['created_date'].month != current_month]


# Create your views here.

def blog_post_list(request):
    context = {
        'latest_posts': get_latest_posts(),
        'oldest_posts': get_oldest_posts(),
    }
    print('list ob post: ', get_latest_posts()[0])
    return render(request, 'blog_post.html', context=context)


def blog_post_details(request, post_id):
    post = get_post_by_id(post_id)

    if not post:
        return HttpResponseNotFound('<h1>Blog post not found</h1>')
    return render(request, 'blog_post_details.html', {'post': post})
