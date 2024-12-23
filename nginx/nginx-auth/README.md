# nginx-auth

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html)
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip). Установите авторизованный вход для учетки: `design:SteveJobs1955`, т.е. логин `design`, пароль `SteveJobs1955`.
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip). Установите авторизованный вход для учетки: `marketing:marketingP@ssword`.
6. Учетка `design` не должна иметь доступ на другие пути, тоже самое касается других учеток.

---

### Ответ

user_design
```bash
design:$1$PRC.uzVY$5K8y7P7cSO95blouUttnd/
```

user_marketing
```bash
marketing:$1$WNEfjRnT$pJhekzGj62pCY2mUsOVnA1
```

```bash
location /images {
        alias /var/www/nginx/cats/;

        auth_basic "Private website";
        auth_basic_user_file conf.d/user_design;
    }

    location /gifs {
        alias /var/www/nginx/gifs;

        autoindex on;
        auth_basic "Private route";
        auth_basic_user_file conf.d/user_marketing;
    }
```