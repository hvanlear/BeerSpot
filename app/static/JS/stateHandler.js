console.log("fuck");
const searchParent = document.querySelector(".searchForm");
const searchInput = document.querySelector(".searchInput");

const state = {
  allBreweries: {
    query: "",
    results: [],
  },
};

// showStateData();

const loadSearchResults = async function (query) {
  try {
    state.allBreweries.query = query;
    const res = await fetch(`${window.origin}/breweries/${query}`);
    const data = await res.json();

    if (!res.ok) throw new Error(`${data.message} (${res.status})`);

    state.allBreweries.results = data.map((item) => {
      return {
        id: item.id,
        name: item.name,
        type: item.brewery_type,
        phone: item.phone,
        state: item.state,
        street: item.street,
        website: item.website_url,
        latitude: item.latitude,
        longitude: item.longitude,
      };
    });
    // console.log(state.allBreweries.query);
    // console.log(state.allBreweries.results);
  } catch (err) {
    console.log("ERROR", err);
    throw err;
  }
};

// const getQuery = function (e) {
//   if (e.target !== e.currentTarget) {
//     let clickedItem = e.target.id;
//     console.log(clickedItem.innerHTML);
//   }
//   e.stopPropagation();
// };

// stateParent.addEventListener("click", getQuery, false);

// class searchView {
//   #parentEl = document.querySelector(".searchForm");
//   getQuery() {
//     return this.#parentEl.querySelector(".searchInput").value;
//   }
//   addHandlerSearch(handler) {
//     this.#parentEl.addEventListener("submit", function (e) {
//       e.preventDefault();
//       handler();
//     });
//   }
// }

const getQuery = function () {
  return searchInput.value;
};

const controlSearchResults = async function () {
  try {
    const query = new searchView.getQuery();
    if (!query) return;
    await loadSearchResults(query);
  } catch (err) {
    console.log(err);
  }
};

searchParent.addEventListener("submit", async function (e) {
  e.preventDefault();
  const query = getQuery();
  if (!query) return;
  await loadSearchResults(query);
  console.log(state.allBreweries.results);
});

// const init = function () {
//   searchView.addHandlerSearch(controlSearchResults);
// };

// init();
