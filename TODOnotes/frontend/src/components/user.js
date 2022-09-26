import React from "react";


const UserItem = ({user, delete_user}) => {
    return (
        <tr>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td><button
                    type='button'
                    onClick={()=>delete_user(user.id)}>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const UserList = ({users, delete_user}) => {
    return (
        <table>
            <th>First name</th>
            <th>Last name</th>
            <th>Email</th>
            {users.map((user) => <UserItem user={user} delete_user={delete_user}/>)}
        </table>
    )
}
export default UserList