import React from 'react'


const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.active}</td>
            <td>{item.title}</td>
            <td>{item.body}</td>
            <td>{item.author}</td>
        </tr>
    )
}

const ToDoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ACTIVE</th>
                <th>TITLE</th>
                <th>BODY</th>
                <th>AUTHOR</th>
            </tr>
            {items.map((item) => <ToDoList item={item} />)}
        </table>
    )
}

export default ToDoList
