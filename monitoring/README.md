Насколько понял из задания, необходимо было сделать только файлы конфигурации. <br>
Достаточно заменить стандартные конфигурационные файлы на те, что представлены в репозитории, после чего нужно перезагрузить сервис **prometheus**:
```
systemctl restart prometheus.service
```
После чего в **prometheus** появится новый target с названием **monitoring** и соответственно по нему будут метрики, их можно визуализировать через graphana (есть dashboard с названием **Prometheus Blackbox Exporter** для этого), но это уже видимо другое задание )
