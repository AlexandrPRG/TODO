import React from "react";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name_project}</td>
            <td>{project.link_project}</td>
            <td>{project.developers}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>Name</th>
            <th>Link</th>
            <th>Devs</th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}
export default ProjectList