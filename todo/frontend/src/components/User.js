import React from 'react'


const UserItem = ({user_set}) => {
    return (
        <tr>
            <td>{user_set.active}</td>
            <td>{user_set.first_name}</td>
            <td>{user_set.last_name}</td>
            <td>{user_set.email}</td>
        </tr>
    )
}

const UserList = ({user_sets}) => {
    return (
        <table>
            <tr>
                <th>active</th>
                <th>first_name</th>
                <th>last_name</th>
                <th>email</th>
            </tr>
            {user_sets.map((user_set) => <UserItem user_set={user_set} />)}
        </table>
    )
}

export default UserList