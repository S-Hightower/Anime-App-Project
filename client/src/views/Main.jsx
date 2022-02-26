import React from "react";

import Header from '../components/Header';
import Search from "../components/Search";

import styles from "./view_css/Main.module.css";

function Main() {
    return (
        <>
        <div className={styles.container}>
            <Header />
            <Search />
        </div>
        </>
    )
}

export default Main;