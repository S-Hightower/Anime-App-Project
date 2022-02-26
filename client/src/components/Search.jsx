import React from "react";

function Search() {
    return (
        <form class="d-flex col-md-6 offset-md-3">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
            <button class="btn btn-dark" type="submit">Search</button>
        </form>
    )
}

export default Search;