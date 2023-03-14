import React from 'react'
import {Link} from 'react-router-dom'

const ToDoItem = ({item, deleteTodo}) => {
    return (
        <tr>
            <td>{item.active}</td>
            <td>{item.title}</td>
            <td>{item.body}</td>
            <td>{item.author}</td>
            <td><button onClick={() => deleteTodo(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const ToDoList = ({items, deleteTodo}) => {
    return (
        <div>
            <table>
                <tr>
                    <th>active</th>
                    <th>title</th>
                    <th>body</th>
                    <th>author</th>
                </tr>
                {items.map((item) => <ToDoList item={item} deleteTodo={deleteTodo} />)}
            </table>
            <Link to='/TODO/create'>Create</Link>
        </div>
    )
}

export default ToDoList
