import React from 'react';
import ReactDOM from 'react-dom';

export default class Footer extends React.Component {


    render() {
        return (
    		<footer>
                <br />
                <br />
                <br />
        		<div>
                    <font style={{ fontSize: '14px'}}>
                        建議您使用Google Chrome、Firefox瀏覽器，並搭配 1024 x 768 以上之螢幕解析度，以獲得最佳瀏覽體驗。
                    </font>
                    <br />
                    <font style={{ fontSize: '14px'}}>
                        We recommend Google Chrome™ or Firefox® browser and set a screen resolution of minimum 1024 x 768 pixels for optimal performance.
                    </font>
                    <br />
                    <br />
                    <font>Copyright (c) 2019 Centers for Disease Control, MOHW, Taiwan (Taiwan CDC).</font>
                </div>
                <br />
                <br />
                <br />
      		</footer>
        );
    }
}