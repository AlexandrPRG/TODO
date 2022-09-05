import React from "react";

const menulink = (MenuLinks) => {}
const Menu = (menu) => {
    return (
    <div>
        <ul>
            <li><a href="menulink">{menu.menuitems[0]}</a></li>
            <li><a href="{{menu.menulinks[0]}}#">{menu.menuitems[1]}</a></li>
            <li><a href="{{menu.menulinks[0]}}">{menu.menuitems[2]}</a></li>
            <li><a href="{{menu.menulinks[0]}}">{menu.menuitems[3]}</a></li>
        </ul>
    </div>
    );
};
export default Menu