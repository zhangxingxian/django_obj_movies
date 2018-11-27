$(function () {

    const URL_POEM = 'http://127.0.0.1:8000/home/film/';
    const IMG_ADDR = '../../static/';
    const DETAIL_URL = 'http://127.0.0.1:8000/home/details/?id='

    // 1 创建xml对象
    let xhr = new XMLHttpRequest();

    // 2 设置访问成功后的处理函数
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let json_str = xhr.responseText;
            let results = JSON.parse(json_str);
            if (results.status === 200) {
                objs = results.data;
                let $leftpart_allinfo = $('.leftpart_allinfo');
                let $rightpart_allinfo = $('.rightpart_allinfo');
                for (let i = 0; i < 12; i++) {
                    $leftpart_allinfo.append(
                        $('<li>')
                            .append(
                                $('<a>').attr('href', DETAIL_URL + objs[i].id)
                                    .append(
                                        $('<img>').attr('src', IMG_ADDR + objs[i].image)
                                    )
                            )
                            .append(
                                $('<p>').text(objs[i].name)
                            )
                            .append(
                                $('<h4>').text(objs[i].type_name + '-' + objs[i].on_decade)
                            )
                    );

                    $rightpart_allinfo.append(
                        $('<li>')
                            .append(
                                $('<a>').attr('href', DETAIL_URL + objs[i].id)
                                    .append(
                                        $('<span>').text(i + 1)
                                    )
                                    .append(
                                        $('<span>').text(objs[12 + i].name)
                                    )
                                    .append(
                                        $('<span>').text(objs[12 + i].update_time.split(' ')[0]))
                            )
                    )

                }


            }
        }
    };

    // 3 打开url连接
    xhr.open('get', URL_POEM);

    // 4 发送请求URL_TEMP
    xhr.send();
});