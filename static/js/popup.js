document.addEventListener("DOMContentLoaded", function() {
    const deleteBtn = document.getElementById("confirm-delete-btn");
    const popup = document.getElementById("popup-overlay");
    const popupConfirm = document.getElementById("popup-confirm");
    const deleteForm = document.getElementById("delete-form");

    if (deleteBtn && popup && popupConfirm && deleteForm) {
        deleteBtn.addEventListener("click", function(event) {
            event.preventDefault(); // μην κάνει submit ακόμα
            popup.style.display = "flex";
        });

        popupConfirm.addEventListener("click", function() {
            deleteForm.submit(); // κάνε submit μόνο αν πατήσει Ναι
        });
    }
});

function closePopup() {
    const popup = document.getElementById("popup-overlay");
    if (popup) popup.style.display = "none";
}
