import React from 'react'
import {
  Link,
  useParams
} from "react-router-dom";

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.repo_link}</td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>REPO_LINK</th>
            </tr>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}

const ProjectUserItem = ({item}) => {
    return (
        <li>
        {item.username} ({item.email})
    </li>
    )
}

const ProjectDetail = ({getProject, item}) => {
    let { id } = useParams();
    getProject(id)
    let users = item.users ? item.users : []
    console.log(id)
    return (
        <div>
            <h1>{item.name}</h1>
            Repository: <a href={item.repository}>{item.repository}</a>
            <p></p>
            Users:
            <ol>
            {users.map((user) => <ProjectUserItem item={user} />)}
            </ol>
        </div>
    )
}

//export {ProjectDetail, ProjectList}

export default ProjectList