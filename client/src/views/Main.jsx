import React from "react";

import Header from '../components/Header';

import styles from "./view_css/Main.module.css";

function Main() {
    return (
        <div className={styles.container}>
            <Header />
        </div>
    )
}

export default Main;