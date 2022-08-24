import React from "react";


const TodoesItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.todo_project}</td>
            <td>{todo.text_note}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.user_todo}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}

const Todoeslist = ({todoes}) => {
    return (
        <table>
            <th>TODO of projects</th>
            <th>Text</th>
            <th>Date creating</th>
            <th>Date updating</th>
            <th>TODO per Developers</th>
            <th>TODO deleted</th>
            {todoes.map((todo) => <TodoesItem todo={todo}/>)}
        </table>
    )
}
export default Todoeslist