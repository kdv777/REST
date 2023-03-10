import React from "react";


const Custom_users_item = ({custom_user}) => {

    return(
        <tr>
            <td>
                {custom_user.username}
            </td>
            <td>
                {custom_user.firstname}
            </td>
            <td>
                {custom_user.lastname}
            </td>
            <td>
                {custom_user.email}
            </td>
        </tr>
    )
}

const Custom_users_list = ({custom_users}) => {

    return(
        <table>
            <th>
                username
            </th>
            <th>
                firstname
            </th>
            <th>
                lastname
            </th>
            <th>
                email
            </th>
            {custom_users.map((custom_user) => <Custom_users_item custom_user={custom_user}/>)}
        </table>
    );
};

export default Custom_users_list;