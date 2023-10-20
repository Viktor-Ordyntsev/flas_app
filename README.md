# flas_app

*Скачивание проета:*
```
git clone <url проекта>
```
*Сборка проета:*
```
docker-compose build
```
*Развертывание проета:*
```
docker-compose up
```
По факту сервис уже рабоатет (по адресу localhost:8000), однако для визуализации данных из бд необходимо настроить подключение pgAdmin
*Настройка pgAdmin:*
```
Заходим по адресу localhost:5050
Вводим логим (root@root.com) и пароль (root)
Далее создаем новое подключение и настраиваем его (Скриншоты ниже)
В поле <Name> вводим любое имя сервера
```
<img width="705" alt="Screenshot 2023-10-20 at 11 26 52" src="https://github.com/Viktor-Ordyntsev/flas_app/assets/132403909/ebd0282b-156c-40a2-bdb5-a24b39c26d52">
\n
```
В поле <Host name/address>  в водим имя контейнера с нашей базой данных
Поля <Username> и <Password> вводим *root*
```
<img width="703" alt="Screenshot 2023-10-20 at 11 27 26" src="https://github.com/Viktor-Ordyntsev/flas_app/assets/132403909/f89e9357-031e-41a0-b5b6-60edecf1d1f0">
