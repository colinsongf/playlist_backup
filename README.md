# 抓取网易云音乐
改用文本存储列表，MySQL存储部分没有完全清除

## 抓取热门歌单
```console
$ python playlist.py  1 10
$ # 抓取热门歌单前十页的歌单名字和链接
```

```console
$ python playlist.py 粤语 1 42
$ # 抓取全部粤语歌单
```

## 抓取歌单内歌曲

```console
$ python music.py playlist 376259016
$ # 抓取编号为 376259016 的歌单
```

```console
$ python music.py database
$ # 抓取存储的热门歌单里面的歌曲，批量抓取
```

## 抓取歌曲评论
```console
$ python comment.py
$ # 自动抓取已存储歌曲，并保持去重复
```

```console
$ python comment.py 407450223
$ # 抓取歌曲编号对应的评论
```

## 数据库结构
- 数据库名字：默认spider
- 数据库配置：配置在spider163.conf的db字段

```console
$ mysql> desc playlist163;
$ +-------------+--------------+------+-----+-------------------+----------------+
$ | Field       | Type         | Null | Key | Default           | Extra          |
$ +-------------+--------------+------+-----+-------------------+----------------+
$ | id          | int(11)      | NO   | PRI | NULL              | auto_increment |
$ | title       | varchar(150) | YES  |     |                   |                |
$ | link        | varchar(120) | YES  |     |                   |                |
$ | cnt         | varchar(20)  | YES  |     | 0                 |                |
$ | dsc         | varchar(50)  | YES  |     | all               |                |
$ | create_time | datetime     | YES  |     | CURRENT_TIMESTAMP |                |
$ | over        | varchar(20)  | YES  | MUL | N                 |                |
$ +-------------+--------------+------+-----+-------------------+----------------+
$ 7 rows in set (0.00 sec)
```
```console
$ mysql> desc music163;
$ +-------------+--------------+------+-----+-------------------+----------------+
$ | Field       | Type         | Null | Key | Default           | Extra          |
$ +-------------+--------------+------+-----+-------------------+----------------+
$ | id          | int(11)      | NO   | PRI | NULL              | auto_increment |
$ | song_id     | int(11)      | YES  |     | NULL              |                |
$ | song_name   | varchar(200) | YES  |     |                   |                |
$ | author      | varchar(350) | YES  |     |                   |                |
$ | over        | varchar(5)   | YES  | MUL | N                 |                |
$ | create_time | datetime     | YES  |     | CURRENT_TIMESTAMP |                |
$ | comment     | int(11)      | YES  |     | 0                 |                |
$ +-------------+--------------+------+-----+-------------------+----------------+
$ 7 rows in set (0.00 sec)
```
```console
$ mysql> desc comment163;
$ +---------+--------------+------+-----+---------+----------------+
$ | Field   | Type         | Null | Key | Default | Extra          |
$ +---------+--------------+------+-----+---------+----------------+
$ | id      | int(11)      | NO   | PRI | NULL    | auto_increment |
$ | song_id | int(11)      | YES  |     | NULL    |                |
$ | txt     | mediumtext   | YES  |     | NULL    |                |
$ | author  | varchar(100) | YES  |     | 注销    |                |
$ | liked   | int(11)      | YES  | MUL | 0       |                |
$ +---------+--------------+------+-----+---------+----------------+
$ 5 rows in set (0.00 sec)
```
```console
$ mysql> desc exception;
$ +-------+--------------+------+-----+---------+----------------+
$ | Field | Type         | Null | Key | Default | Extra          |
$ +-------+--------------+------+-----+---------+----------------+
$ | id    | int(11)      | NO   | PRI | NULL    | auto_increment |
$ | eid   | int(11)      | YES  |     | 0       |                |
$ | scene | varchar(300) | YES  |     | NULL    |                |
$ | tb    | varchar(30)  | YES  |     | NULL    |                |
$ +-------+--------------+------+-----+---------+----------------+
$ 4 rows in set (0.00 sec)
```

# TODO
- 增加抓取歌单页面个性推荐歌单
- 增加抓取排行榜 ✔️
- 严格去重复 ✔️
- 优化代码结构，冗余代码过多

# BUG
- 若干歌单无法抓取，待重现定位
- ...

# THANKS
- 给网易一个大感谢！

# 欢迎关注微信公众账号：程天写代码
![guojingcoooool](https://github.com/Chengyumeng/spider163/blob/master/wechat.jpeg)
