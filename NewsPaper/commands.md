1. Создать двух пользователей
User.objects.create(username = 'User_1', password = '777', first_name = 'Гарри', last_name = 'Поттер', email = 'scar@gail.com')
User.objects.create(username = 'User_2', password = '888', first_name = 'Фродо', last_name = 'Бэггинс', email = 'ring@gmail.com')

2. Создать два объекта модели Author
Author.objects.create(User = User.objects.get(username='User_2'))

3. Добавить 4 категории в модель Category
Category.objects.create(cat_name='IT')
Category.objects.create(cat_name='Животные')
Category.objects.create(cat_name='Спорт')
Category.objects.create(cat_name='Кино и сералы')

4. Добавить 2 статьи и 1 новость
Post.objects.create(author = Author(pk=1), post_type='AR', header = '100 ответов на вопросы об IT', body = 'Ответы на вопросы')
Post.objects.create(author = Author(pk=2), post_type='AR', header = 'Спорт будущего', body = 'статья про кмберспорт')
Post.objects.create(author = Author(pk=2), post_type='NE', header = 'Феноменальный прорыв в кино', body = 'Новости о кино')

5. Присвоить им категории
Post_Category.objects.create(posts = Posts.objects.get(pk=1), categories = Categories.objects.get(cat_name = 'IT'))
Post_Category.objects.create(posts = Posts.objects.get(pk=2), categories = Categories.objects.get(cat_name = 'Животные'))
Post_Category.objects.create(posts = Posts.objects.get(pk=3), categories = Categories.objects.get(cat_name = 'Спорт'))
Post_Category.objects.create(posts = Posts.objects.get(pk=4), categories = Categories.objects.get(cat_name = 'Фильмы и сериалы'))

6. Создать как минимум 4 комментария к разным объектам модели Post
Comments.objects.create(posts = Posts.objects.get(pk=1), user = User.objects.get(username = 'User_1'), text_comment = '1 комментарий')
Comments.objects.create(posts = Posts.objects.get(pk=2), user = User.objects.get(username = 'User_2'), text_comment = '2 комментарий')
Comments.objects.create(posts = Posts.objects.get(pk=3), user = User.objects.get(username = 'User_3'), text_comment = '3 комментарий')
Comments.objects.create(posts = Posts.objects.get(pk=3), user = User.objects.get(username = 'User_1'), text_comment = '4 комментарий')

7. Применить функции like() и dislike() к статьям/новостям и комментариям
Comments.objects.get(pk=1).like()
Comments.objects.get(pk=2).dislike()
Comments.objects.get(pk=3).like()
Comments.objects.get(pk=4).dilike()
Posts.objects.get(pk=1).like()
Posts.objects.get(pk=2).dislike()
Posts.objects.get(pk=3).like()
Posts.objects.get(pk=2).dislike()

8. Обновить рейтинги пользователей
Authors.objects.get(pk=1).update_rating()
Authors.objects.get(pk=2).update_rating()

9. Вывести username и рейтинг лучшего пользователя
Authors.objects.all().order_by('-rating').values('user', 'rating')[0]

10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи
Posts.objects.all().order_by('-rate_post').values('date_create', 'authors', 'rate_post', 'header')[0]
top_rate = Posts.objects.all().order_by('-rate_post')[0]
top_rate.preview()

11. Вывести все комментарии
Comments.objects.all().values('date_create', 'user', 'rate_comment', 'text_comment')