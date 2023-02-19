import React from 'react'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>{user.project}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>FIRST_NAME</th>
                <th>LAST_NAME</th>
                <th>EMAIL</th>
                <th>PROJECT</th>
            </tr>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList