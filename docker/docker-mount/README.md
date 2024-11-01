# docker-mount

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-mount`.
2. Скачать конфигурационный файл [jusan-docker-mount.conf][jusan-docker-mount-conf] с помощью `curl`.
3. Скачать конфигурационный файл [jusan-docker-mount.zip][jusan-docker-mount-zip] с помощью `curl`.
   Разархивировать архив с помощью `unzip`.
4. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 9999 на 80 порт контейнера;
   - имя контейнера `jusan-docker-mount`;
   - монтирует скачанный `jusan-docker-mount.conf` внутрь контейнера `/etc/nginx/conf.d/jusan-docker-mount.conf`;
   - монтирует распакованный `jusan-docker-mount.zip` внутрь контейнера. Определите куда нужно монтировать по конфигурационному файлу;
   - использует образ `nginx:mainline`.

5. Проверьте запросы с помощью `curl`:

   - `http://localhost:9999` - ожидаемый ответ: `<h1>Hello, from jusan-docker-mount</h1>`;
   - `http://localhost:9999/test` - ожидаемый ответ: `Singularity`;
   - `http://localhost:9999/token` - ожидаемый ответ: `Jusan`;

6. Посмотрите на логи `nginx`:

```bash
docker logs jusan-docker-mount
```

7. Все выполненные команды начиная со 2 шага, кроме 5 и 6, записать в файл `docker-mount/solution.sh`.

8. Запушить в репозиторий `jusan-docker`. В папке `docker-mount` должны быть:
   - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[jusan-docker-mount-conf]: https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
[jusan-docker-mount-zip]: https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-mount.sh

---

### Ответ

1. Скачивание файлов
```bash
curl -LJO https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
curl -LJO https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
```

2. Распаковка
```bash
unzip jusan-docker-mount.zip -d .
```

3. Запускаем контейнер и монитируем конфиги
```bash
docker run -d --name jusan-docker-mount -p 9999:80 \
    --mount type=bind,source="$(pwd)"/jusan-docker-mount.conf,target=/etc/nginx/conf.d/jusan-docker-mount.conf \
    --mount type=bind,source="$(pwd)"/jusan-docker-mount,target=/var/www/example \
    nginx:mainline
```

4. Удаляем конфиг по умолчанию, который находится внутри контейнера и перезапускаем nginx
```bash
docker exec jusan-docker-mount rm /etc/nginx/conf.d/default.conf
docker exec jusan-docker-mount nginx -s reload
```
