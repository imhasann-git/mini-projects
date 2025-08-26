// ===== LocalStorage Helpers =====
function getNotes() {
  return JSON.parse(localStorage.getItem("notes")) || [];
}

function saveNotes(notes) {
  localStorage.setItem("notes", JSON.stringify(notes));
}

// ===== DOM Elements =====
const submitBtn = document.getElementById("submit-input");
const titleInput = document.getElementById("title-input");
const descInput = document.getElementById("desc-input");
const notesContainer = document.getElementById("notes-container");

const editModal = document.getElementById("edit-modal");
const editTitle = document.getElementById("edit-title");
const editDescription = document.getElementById("edit-description");
const editContent = document.getElementById("edit-content");
const saveEditBtn = document.getElementById("save-edit");
const cancelEditBtn = document.getElementById("cancel-edit");

let currentNoteId = null;

// ===== Add New Note =====
submitBtn.addEventListener("click", () => {
  const title = titleInput.value.trim();
  const description = descInput.value.trim();

  if (!title && !description) return;

  const newNote = {
    id: Date.now().toString(),
    title: title || "Untitled",
    description: description || "No description",
    content: "",
  };

  const notes = getNotes();
  notes.push(newNote);
  saveNotes(notes);

  renderNotes();
  //reseting the values
  titleInput.value = "";
  descInput.value = "";
});

// ===== Render Notes =====
function renderNotes() {
  notesContainer.innerHTML = "";
  const notes = getNotes();

  notes.forEach((note) => {
    const noteDiv = document.createElement("div");
    noteDiv.className = "bg-indigo-900 rounded-md mx-2 my-2 gap-2 flex-grow";
    noteDiv.id = note.id;

    noteDiv.innerHTML = `
      <div class="flex justify-between items-center px-2 py-2 group">
        <h2 class="text-white bg-transparent font-mono">${note.title}</h2>
        <div class="gap-2 hidden group-hover:flex">
          <button
            class="text-white hover:text-yellow-400 transition-colors edit-btn"
            title="Edit"
            data-note-id="${note.id}"
          >
            <i class="fa-solid fa-pen-to-square"></i>
          </button>
          <button
            class="text-white hover:text-red-500 transition-colors delete-btn"
            title="Delete"
            data-note-id="${note.id}"
          >
            <i class="fa-solid fa-trash"></i>
          </button>
        </div>
      </div>
      <p class="text-white py-2 px-2 font-mono">${note.description}</p>
      <div
        class="text-gray-300 py-2 px-2 font-mono text-sm hidden"
        id="note-content"
      >
        ${note.content || ""}
      </div>
    `;

    notesContainer.appendChild(noteDiv);
  });
}

// ===== Open Edit Modal =====
document.addEventListener("click", function (e) {
  if (e.target.closest(".edit-btn")) {
    const editBtn = e.target.closest(".edit-btn");
    currentNoteId = editBtn.getAttribute("data-note-id");
    openEditModal(currentNoteId);
  }

  if (e.target.closest(".delete-btn")) {
    const deleteBtn = e.target.closest(".delete-btn");
    const noteId = deleteBtn.getAttribute("data-note-id");
    deleteNote(noteId);
  }
});

function openEditModal(noteId) {
  const notes = getNotes();
  const note = notes.find((n) => n.id === noteId);

  if (note) {
    editTitle.value = note.title;
    editDescription.value = note.description;
    editContent.value = note.content;

    editModal.classList.remove("hidden");
    editTitle.focus();
  }
}

function closeEditModal() {
  editModal.classList.add("hidden");
  currentNoteId = null;
  editTitle.value = "";
  editDescription.value = "";
  editContent.value = "";
}

// ===== Save Changes in Edit Modal =====
saveEditBtn.addEventListener("click", function () {
  if (!currentNoteId) return;

  const notes = getNotes();
  const noteIndex = notes.findIndex((n) => n.id === currentNoteId);

  if (noteIndex !== -1) {
    notes[noteIndex].title = editTitle.value || "Untitled";
    notes[noteIndex].description = editDescription.value || "No description";
    notes[noteIndex].content = editContent.value || "";

    saveNotes(notes);
    renderNotes();
    closeEditModal();
  }
});

// ===== Cancel Edit =====
cancelEditBtn.addEventListener("click", closeEditModal);

// ===== Delete Note =====
function deleteNote(noteId) {
  let notes = getNotes();
  notes = notes.filter((n) => n.id !== noteId);
  saveNotes(notes);
  renderNotes();
}

// ===== Initial Render on Page Load =====
document.addEventListener("DOMContentLoaded", renderNotes);
