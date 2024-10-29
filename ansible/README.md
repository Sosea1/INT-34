## Ansible
---
### Предварительная настройка хоста
---
1. Установка `opensh-server`:
   ```
   sudo apt update
   sudo apt install openssh-server
   sudo systemctl enable ssh
   sudo systemctl start ssh
   ```
3. Добавить нового пользователя `ansible`:
   ```
   sudo adduser ansible
   ```
4. В `etc/sudoers` добавить следующую строчку:
   ```
   ansible ALL=(ALL:ALL) NOPASSWD:ALL
   ```
---
## Описание playbook
---
playbook настраивает следующее:
- устанавливает базовые утилиты;
- настраивает фаервол (запрещает все соединения кроме http, https, ssh и postgresql);
- настраивает sysctl, например включает tcp_syncookies - технику противодействия SYN-флуд атаке;
- создает новые группы admins и users и соответствующих пользователей;
- настраивает ssh - запрещает удаленный вход в систему для пользователя root;
- устанавливает и настраивает PostgreSQL;
- установаливает и настривает fail2ban.

---
### Запуск playbook
В файле **inventory.yml** необходимо прописать ip адрес настраиваемого хоста. <br>
Для запуска playbook используется команда:
```
ansible-playbook playbook.yaml
```
Все переменные прописаны в inventory, можно и в .env было, но так я думаю будет удобнее проверять
Для проверки подключения к **PostgreSQL**:
```
psql -U postgres -h <host_ip> -p 5432
```
