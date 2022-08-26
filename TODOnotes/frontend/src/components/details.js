import React from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";


const UserItem = ({ user }) => {
    let { id } = useParams()
    console.log(id)
    console.log(useParams)
    let filter_todoes = user.filter((todo => todo.todo.users.includes(parseInt(id))))
    return (
        <tr>
            <td><Link to={`/user/${user.id}`}>{user.first_name}</Link></td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
            )
}

            const UserTodoes = ({todoes}) => {
    return (
            <table>
                <th>First name</th>
                <th>Last name</th>
                <th>Email</th>
                {todoes.map((user) => <UserItem user={user} />)}
            </table>
            )
}
            export default UserTodoes