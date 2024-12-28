# superjob.ru
Скрипт обновляет резюме на сайте superjob.ru

Инструкция (все подробности на https://api.superjob.ru/)
1. Зарегистрируйте приложение на сайте: https://api.superjob.ru/info/ (с получением Secret Key),
2. Пройдите авторизацию (возможно в строке браузера) по ссылке GET https://www.superjob.ru/authorize/?client_id=3690&redirect_uri=http%3A%2F%2Fwww.example.ru&state=custom в которую подставлены значения client_id (на странице из п. 1) и сайт, куда вернётся параметр code (в строке браузера),
3. Запросите access_token и refresh_token по ссылке GET https://api.superjob.ru/2.0/oauth2/access_token/?code=c907a&redirect_uri=http%3A%2F%2Fwww.example.ru&client_id=3690&client_secret=v3.r.127479810.b87cf065c96f30ca2605629670c86ac48bef1b50.adaaf7159e815a48fdeb39244791082f40cc3735 в которую подставлены значения code из п.2, redirect_uri и client_id из п.1, а также client_secret со страницы зарегистрированного приложения,
4. Подставьте возвращенные параметры в файл .env проекта, заменив находящиеся там тестовые данные, а также подставьте туда свой токен бота и CHAT_ID в телеграмме. Регистрация своего бота подробно описана на сторонних ресурсах, для получения CHAT_ID своего аккаунта существуют специальные боты. Не забудьте, что зарегистрированному боту необходимо отправить хотя бы одно сообщение, иначе уведомления приходить не будут,
5. Проверьте, что установлены библиотеки telebot, requests, а также python-dotenv, 
6. Запускайте скрипт каждый час, подставив в crontab значения вида 0       */2       *           *           *       /usr/local/bin/python3 /usr/home/test/sj/superjob.py (не забыв указать свои пути к интерпретатору и скрипту, а также проверив права на перезапись файла .env). 
