import React from "react";


const Menu = (menu) => {
    return (
    <div>
        <ul
//        style="margin: 0; padding: 0; list-style-type: none;"
         >
            <li
//              style="display: inline;"
            >
                <a href="#">{menu.menuitem[0]}</a></li>
            <li><a href="#">{menu.menuitem[1]}</a></li>
            <li><a href="#">{menu.menuitem[2]}</a></li>
        </ul>
    </div>
    );
};
export default Menu