# docker-bind

### Полезное

- [Use bind mounts](https://docs.docker.com/storage/bind-mounts/)

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-bind`.
2. Скачать конфигурационный файл [nginx.conf](./nginx.conf) с помощью `curl`.
3. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 7777 на 80 порт контейнера;
   - имя контейнера `jusan-docker-bind`;
   - монтирует скачанный `nginx.conf` внутрь контейнера `/etc/nginx/nginx.conf`;
   - использует образ `nginx:mainline`.

4. Проверьте запрос `http://localhost:7777` с помощью `curl`. В ответ должно прийтие `Привет из Docker контейнера! 🐳`.
5. Посмотрите список запущенных контейнеров. Проверьте в списке, как отображается контейнер `jusan-docker-bind`.
6. Посмотрите на логи `nginx` командой:

```bash
docker logs jusan-docker-bind
```

7. Все выполненные команды в шаге 2 и 3 записать в файл `docker-bind/solution.sh`.

8. Запушить в репозиторий `jusan-docker`. В папке `docker-bind` должны быть:
   - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-bind.sh

---

### Ответ

1. Для скачивания используя curl:
```console
curl -LJO https://raw.githubusercontent.com/Smagicom/TechOrda/refs/heads/main/docker/docker-bind/nginx.conf
```

2. Монитирование с --mount
```console
docker run -d --name jusan-docker-bind -p 7777:80 --mount type=bind,source="$(pwd)"/nginx.conf,target=/etc/nginx/nginx.conf nginx:mainline
```

3. Монтирование с -volume
```bash
docker run -d --name jusan-docker-bind -p 7777:80 -v "$(pwd)"/nginx.conf:/etc/nginx/nginx.conf nginx:mainline
```