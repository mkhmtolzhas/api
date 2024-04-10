const searchArticles = () => {
    const searchInputValue = document.getElementById("searchArticles").value;
    window.location.href = `${searchInputValue}`
}
const redirectToMainPage = () => {
    window.location.href = "http://127.0.0.1:8000/"
}