function showSection(sectionId) {
    document.querySelectorAll('.section').forEach(section => {
        section.style.display = 'none';
    });
    document.getElementById(sectionId).style.display = 'block';
}

function loadProduits() {
    fetch('/produits')
        .then(response => response.json())
        .then(data => {
            const produitsList = document.getElementById('liste-produits');
            produitsList.innerHTML = '';
            data.forEach(produit => {
                const li = document.createElement('li');
                li.textContent = `${produit.nom} - ${produit.prix}€ (Stock ID: ${produit.stock_id})`;
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Supprimer';
                deleteButton.onclick = () => deleteProduit(produit.id);
                li.appendChild(deleteButton);
                produitsList.appendChild(li);
            });
        });
}

function deleteProduit(id) {
    fetch(`/produits/${id}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                alert('Produit supprimé avec succès !');
                loadProduits();
            } else {
                alert('Erreur lors de la suppression du produit.');
            }
        });
}

function loadVentes() {
    fetch('/ventes')
        .then(response => response.json())
        .then(data => {
            const ventesList = document.getElementById('liste-ventes');
            ventesList.innerHTML = '';
            data.forEach(vente => {
                const li = document.createElement('li');
                li.textContent = `Vente #${vente.id} - ${vente.montant_total}€ (Client ID: ${vente.client_id})`;
                const detailsButton = document.createElement('button');
                detailsButton.textContent = 'Détails';
                detailsButton.onclick = () => showDetailsVente(vente.id);
                li.appendChild(detailsButton);
                ventesList.appendChild(li);
            });
        });
}

function showDetailsVente(id) {
    fetch(`/ventes/${id}`)
        .then(response => response.json())
        .then(data => {
            alert(`Détails de la vente #${data.id}:\nMontant: ${data.montant_total}€\nClient ID: ${data.client_id}`);
        });
}


function loadFournisseurs() {
    fetch('/fournisseurs')
        .then(response => response.json())
        .then(data => {
            const fournisseursList = document.getElementById('liste-fournisseurs');
            fournisseursList.innerHTML = '';
            data.forEach(fournisseur => {
                const li = document.createElement('li');
                li.textContent = `${fournisseur.nom} - ${fournisseur.contact}`;
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Supprimer';
                deleteButton.className = 'danger';
                deleteButton.onclick = () => deleteFournisseur(fournisseur.id);
                li.appendChild(deleteButton);
                fournisseursList.appendChild(li);
            });
        });
}

function deleteFournisseur(id) {
    fetch(`/fournisseurs/${id}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                alert('Fournisseur supprimé avec succès !');
                loadFournisseurs();
            } else {
                alert('Erreur lors de la suppression du fournisseur.');
            }
        });
}

document.getElementById('ajouter-fournisseur').addEventListener('submit', function (e) {
    e.preventDefault();
    const nom = document.getElementById('nom-fournisseur').value;
    const contact = document.getElementById('contact-fournisseur').value;

    fetch('/fournisseurs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nom, contact }),
    })
        .then(response => response.json())
        .then(data => {
            alert('Fournisseur ajouté avec succès !');
            loadFournisseurs();
        })
        .catch(error => {
            console.error('Erreur:', error);
        });
});

document.getElementById('ajouter-produit').addEventListener('submit', function (e) {
    e.preventDefault();
    const nom = document.getElementById('nom').value;
    const prix = document.getElementById('prix').value;
    const stock_id = document.getElementById('stock_id').value;

    fetch('/produits', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nom, prix, stock_id }),
    })
        .then(response => response.json())
        .then(data => {
            alert('Produit ajouté avec succès !');
            loadProduits();
        })
        .catch(error => {
            console.error('Erreur:', error);
        });
});

document.addEventListener('DOMContentLoaded', function () {
    showSection('accueil');
});

function setActiveMenu(sectionId) {
    document.querySelectorAll('nav ul li a').forEach(link => {
        link.classList.remove('active');
    });
    document.querySelector(`nav ul li a[onclick*="${sectionId}"]`).classList.add('active');
}

function showSection(sectionId) {
    document.querySelectorAll('.section').forEach(section => {
        section.style.display = 'none';
    });
    document.getElementById(sectionId).style.display = 'block';
    setActiveMenu(sectionId);
}