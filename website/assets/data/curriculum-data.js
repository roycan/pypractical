/* =====================================================================
   curriculum-data.js — curated map of stages → families → problems.
   Sourced from the repo's metadata.yml files + CURRICULUM.md.
   Stage↔family mapping is the editorial default (see plans/website-plan.md §7.3);
   trivial to adjust here.
   ===================================================================== */
window.PYPRA_CURRICULUM = {
  stats: { problems: 41, families: 11, tests: 473 },

  // Distribution tiers (governance): "reference" families are public demos;
  // all other families are "pack" — educator-distributed, never deep-linked
  // from the public site (which shows metadata only). See website/README.md.
  referenceFamilies: ["f01"],

  stages: [
    {
      id: "s1", num: 1, title: "Thinking Like a Programmer",
      concepts: ["Variables", "Input & Output", "Arithmetic", "Conditionals", "Loops", "Functions"],
      blurb: "Students learn the fundamental building blocks — a computer follows precise instructions, and programs are built from small, understandable pieces.",
      families: ["f01"]
    },
    {
      id: "s2", num: 2, title: "Thinking About Objects",
      concepts: ["Classes", "Objects", "Attributes", "Methods"],
      blurb: "Students begin modeling the real world — discovering that software can be organized around the things it represents.",
      families: ["f02", "f03", "f04"]
    },
    {
      id: "s3", num: 3, title: "Objects Working Together",
      concepts: ["Lists of Objects", "Searching", "Updating", "Collaboration"],
      blurb: "Collections become meaningful because they represent groups of real things. Students write software that resembles small real-world applications.",
      families: ["f09"]
    },
    {
      id: "s4", num: 4, title: "Building Better Software",
      concepts: ["Inheritance", "Polymorphism", "Composition", "Code Reuse"],
      blurb: "Programming becomes less about writing code and more about designing systems. Families focus on software organization rather than larger algorithms.",
      families: ["f05", "f06", "f07", "f08", "f10", "f11"]
    },
    {
      id: "s5", num: 5, title: "Data and Algorithms",
      concepts: ["Searching", "Sorting", "Dictionaries", "Files"],
      blurb: "Only after students can create correct software do we ask them to improve it — efficiency becomes meaningful once correctness is understood.",
      families: []
    },
    {
      id: "s6", num: 6, title: "Projects",
      concepts: ["Planning", "Designing", "Implementing", "Testing", "Debugging", "Improving"],
      blurb: "The curriculum culminates in projects that combine everything — experiences that feel like accomplishments rather than examinations.",
      families: []
    }
  ],

  families: {
    "f01": {
      id: "f01", num: 1, folder: "Family-01-Minimum-Cost", title: "Minimum Cost",
      stage: "s1", difficulty: 1,
      blurb: "Compute the cheaper of two billing models — the everyday skill of picking the lowest price.",
      problems: [
        { slug: "01-Parking-Garage", title: "Parking Garage Daily Report", difficulty: 1, time: "15 min", tested: true, concepts: ["variables","arithmetic","if","loops","accumulators","functions"] },
        { slug: "02-Internet-Cafe", title: "Internet Cafe", difficulty: 1, time: "15 min", tested: true, concepts: ["variables","arithmetic","if","loops","accumulators","functions"] }
      ]
    },
    "f02": {
      id: "f02", num: 2, folder: "Family-02-Intro-OOP", title: "Intro to OOP",
      stage: "s2", difficulty: 1,
      blurb: "First steps modeling the world as objects — define a class, give it data and behavior.",
      problems: [
        { slug: "01-Product-Catalog", title: "Product Catalog", difficulty: 1, time: "15 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors"] },
        { slug: "02-Book-Inventory", title: "Book Inventory", difficulty: 1, time: "15 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors"] },
        { slug: "03-Ticket-Sales", title: "Ticket Sales", difficulty: 1, time: "15 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors"] },
        { slug: "04-Seed-Order", title: "Seed Order", difficulty: 1, time: "15 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors"] }
      ]
    },
    "f03": {
      id: "f03", num: 3, folder: "Family-03-Classes-and-Objects", title: "Classes and Objects",
      stage: "s2", difficulty: 2,
      blurb: "Build small schedulers and recorders where objects cooperate to get a job done.",
      problems: [
        { slug: "01-TV-Recorder", title: "TV Recorder Scheduler", difficulty: 2, time: "20 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors"] },
        { slug: "02-Meeting-Room-Scheduler", title: "Meeting Room Scheduler", difficulty: 2, time: "20 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors","object collaboration"] },
        { slug: "03-Interview-Scheduler", title: "Interview Scheduler", difficulty: 2, time: "20 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors","object collaboration"] },
        { slug: "04-Studio-Booking", title: "Studio Booking", difficulty: 2, time: "20 min", tested: false, concepts: ["classes","objects","instance variables","methods","constructors","object collaboration"] }
      ]
    },
    "f04": {
      id: "f04", num: 4, folder: "Family-04-Encapsulation", title: "Encapsulation",
      stage: "s2", difficulty: 2,
      blurb: "Protect an object's data behind methods — learn accessors and controlled state.",
      problems: [
        { slug: "01-Bank-Account", title: "Bank Account", difficulty: 2, time: "20 min", tested: false, concepts: ["encapsulation","classes","objects","instance variables","methods","accessors"] },
        { slug: "02-Fuel-Tank", title: "Fuel Tank", difficulty: 2, time: "20 min", tested: false, concepts: ["encapsulation","classes","objects","instance variables","methods","accessors"] },
        { slug: "03-Piggy-Bank", title: "Piggy Bank", difficulty: 2, time: "20 min", tested: false, concepts: ["encapsulation","classes","objects","instance variables","methods","accessors"] },
        { slug: "04-Water-Tank", title: "Water Tank", difficulty: 2, time: "20 min", tested: false, concepts: ["encapsulation","classes","objects","instance variables","methods","accessors"] }
      ]
    },
    "f05": {
      id: "f05", num: 5, folder: "Family-05-Inheritance", title: "Inheritance",
      stage: "s4", difficulty: 2,
      blurb: "Share behavior across related types using subclasses and hierarchies.",
      problems: [
        { slug: "01-Staff-Hierarchy", title: "Staff Hierarchy", difficulty: 2, time: "20 min", tested: false, concepts: ["inheritance","subclasses","classes","objects","methods","constructors"] },
        { slug: "02-Vehicle-Hierarchy", title: "Vehicle Hierarchy", difficulty: 2, time: "20 min", tested: false, concepts: ["inheritance","subclasses","classes","objects","methods","constructors"] },
        { slug: "03-Team-Roster", title: "Team Roster", difficulty: 2, time: "20 min", tested: false, concepts: ["inheritance","subclasses","classes","objects","methods","constructors"] },
        { slug: "04-Pet-Registry", title: "Pet Registry", difficulty: 2, time: "20 min", tested: false, concepts: ["inheritance","subclasses","classes","objects","methods","constructors"] }
      ]
    },
    "f06": {
      id: "f06", num: 6, folder: "Family-06-Method-Overriding", title: "Method Overriding",
      stage: "s4", difficulty: 3,
      blurb: "Specialize inherited behavior by overriding methods in subclasses.",
      problems: [
        { slug: "01-Shipping-Cost", title: "Shipping Cost", difficulty: 3, time: "20 min", tested: false, concepts: ["method overriding","inheritance","subclasses","classes","objects","methods"] },
        { slug: "02-Parking-Fee", title: "Parking Fee", difficulty: 3, time: "20 min", tested: false, concepts: ["method overriding","inheritance","subclasses","classes","objects","methods"] },
        { slug: "03-Ticket-Price", title: "Ticket Price", difficulty: 3, time: "20 min", tested: false, concepts: ["method overriding","inheritance","subclasses","classes","objects","methods"] },
        { slug: "04-Rental-Cost", title: "Rental Cost", difficulty: 3, time: "20 min", tested: false, concepts: ["method overriding","inheritance","subclasses","classes","objects","methods"] }
      ]
    },
    "f07": {
      id: "f07", num: 7, folder: "Family-07-Polymorphism", title: "Polymorphism",
      stage: "s4", difficulty: 3,
      blurb: "Treat different objects the same way through a shared method — one call, many behaviors.",
      problems: [
        { slug: "01-Price-Cart", title: "Price Cart", difficulty: 3, time: "20 min", tested: false, concepts: ["polymorphism","duck typing","classes","objects","methods","loops"] },
        { slug: "02-Points-Board", title: "Points Board", difficulty: 3, time: "20 min", tested: false, concepts: ["polymorphism","duck typing","classes","objects","methods","loops"] },
        { slug: "03-Fee-Report", title: "Fee Report", difficulty: 3, time: "20 min", tested: false, concepts: ["polymorphism","duck typing","classes","objects","methods","loops"] },
        { slug: "04-Weight-Scale", title: "Weight Scale", difficulty: 3, time: "20 min", tested: false, concepts: ["polymorphism","duck typing","classes","objects","methods","loops"] }
      ]
    },
    "f08": {
      id: "f08", num: 8, folder: "Family-08-Abstraction", title: "Abstraction",
      stage: "s4", difficulty: 3,
      blurb: "Define common contracts with abstract classes and abstract methods.",
      problems: [
        { slug: "01-Shapes", title: "Shapes", difficulty: 3, time: "20 min", tested: false, concepts: ["abstraction","abstract methods","inheritance","subclasses","classes","objects"] },
        { slug: "02-Land-Area", title: "Land Area", difficulty: 3, time: "20 min", tested: false, concepts: ["abstraction","abstract methods","inheritance","subclasses","classes","objects"] },
        { slug: "03-Fabric-Order", title: "Fabric Order", difficulty: 3, time: "20 min", tested: false, concepts: ["abstraction","abstract methods","inheritance","subclasses","classes","objects"] },
        { slug: "04-Screen-Grid", title: "Screen Grid", difficulty: 3, time: "20 min", tested: false, concepts: ["abstraction","abstract methods","inheritance","subclasses","classes","objects"] }
      ]
    },
    "f09": {
      id: "f09", num: 9, folder: "Family-09-Relationships-Association", title: "Relationships — Association",
      stage: "s3", difficulty: 3,
      blurb: "Model one-to-many relationships where objects reference and use each other.",
      problems: [
        { slug: "01-Library", title: "Library", difficulty: 3, time: "20 min", tested: false, concepts: ["object relationships","association","one-to-many","classes","objects","lists","methods"] },
        { slug: "02-Classroom", title: "Classroom", difficulty: 3, time: "20 min", tested: false, concepts: ["object relationships","association","one-to-many","classes","objects","lists","methods"] },
        { slug: "03-Playlist", title: "Playlist", difficulty: 3, time: "20 min", tested: false, concepts: ["object relationships","association","one-to-many","classes","objects","lists","methods"] },
        { slug: "04-Team-Roster", title: "Team Roster", difficulty: 3, time: "20 min", tested: false, concepts: ["object relationships","association","one-to-many","classes","objects","lists","methods"] }
      ]
    },
    "f10": {
      id: "f10", num: 10, folder: "Family-10-Relationships-Composition", title: "Relationships — Composition",
      stage: "s4", difficulty: 4,
      blurb: "Build complex objects that own and manage their parts.",
      problems: [
        { slug: "01-Flashlight", title: "Flashlight", difficulty: 4, time: "25 min", tested: false, concepts: ["composition","object ownership","whole-part relationship","classes","objects","lists","loops"] },
        { slug: "02-Storage-Crate", title: "Storage Crate", difficulty: 4, time: "25 min", tested: false, concepts: ["composition","object ownership","whole-part relationship","classes","objects","lists","loops"] },
        { slug: "03-Computer-Memory", title: "Computer Memory", difficulty: 4, time: "25 min", tested: false, concepts: ["composition","object ownership","whole-part relationship","classes","objects","lists","loops"] },
        { slug: "04-Passenger-Train", title: "Passenger Train", difficulty: 4, time: "25 min", tested: false, concepts: ["composition","object ownership","whole-part relationship","classes","objects","lists","loops"] }
      ]
    },
    "f11": {
      id: "f11", num: 11, folder: "Family-11-SOLID-Single-Responsibility", title: "SOLID — Single Responsibility",
      stage: "s4", difficulty: 4,
      blurb: "Design classes with one clear reason to change — the first of the SOLID principles.",
      problems: [
        { slug: "01-Sale-Receipt", title: "Sale Receipt", difficulty: 4, time: "25 min", tested: false, concepts: ["single responsibility principle","SOLID","separation of concerns","classes","objects","methods"] },
        { slug: "02-Score-Report", title: "Score Report", difficulty: 4, time: "25 min", tested: false, concepts: ["single responsibility principle","SOLID","separation of concerns","classes","objects","methods"] },
        { slug: "03-Inventory-Tag", title: "Inventory Tag", difficulty: 4, time: "25 min", tested: false, concepts: ["single responsibility principle","SOLID","separation of concerns","classes","objects","methods"] }
      ]
    }
  }
};
