<!-- source: https://github.com/ocornut/imgui/wiki/Docking
     fetched: 2026-09-19
     licence: MIT — https://github.com/ocornut/imgui/blob/master/LICENSE.txt
     title: Dear ImGui wiki — Docking
     version: Dear ImGui 1.93.0 WIP (master, 2026-09-19) -->

- Search Issues: https://github.com/ocornut/imgui/labels/docking
- See: [Glossary -> Docking terms](Glossary#docking-terms).

![Docked windows](https://user-images.githubusercontent.com/8225057/97541627-c0dea300-19c5-11eb-9416-8bb255e189a1.png)
<BR>_Docked windows_

## Preamble

#### Where to find it?

Docking is currently available in the [docking](https://github.com/ocornut/imgui/tree/docking) branch. 
- This is a well maintained branch and most large teams have been using this branch for a while. 
- It is safe and recommended to use that branch. 
- The branch also include the [Multi-viewports](https://github.com/ocornut/imgui/wiki/Multi-Viewports) feature.
- Since July 2023, releases are also tagged for docking, e.g. `v1.92.0` `v1.92.0-docking`.

#### How can I enable docking?

Enable config flag:
- `ImGui::GetIO().ConfigFlags |= ImGuiConfigFlags_DockingEnable;`

Create a fullscreen dockspace (optional)
- `ImGui::DockSpaceOverViewport();`

That's pretty much it.
There are additional docked related configuration flags in the ImGuiIO structure which you may toy with.

#### Why is not merged to master???

(This is the most asked question ever)
<BR>TL;DR; I am not happy with the current state of the code. I am a cautious person.

- I want to rewrite it from scratch a third time (1st version was never released).
- DockBuilder API is kept in imgui_internal.h because it is not great.
- Many open issues don't have easy enough fixes, which suggests the code being too complex or fragile compared to the quality I strive for.
- Some core concepts needs to be re-implemented or redesigned. 
- I have been incrementally adding automated tests to [imgui_test_suite](https://github.com/ocornut/imgui_test_engine) in order to facilitate rewriting the code.

However, you can benefit from a lot of docking features without being impacted by any of this. **The largest amount of interactions you'll have with the docking system are at end-user level and do not require API calls**. By just enabling the config flag above and calling a few functions you can benefit from 90% of Docking features. Even the hypothetical full rewrite of Docking system is not expected to impact most users. API that are most at risk of changing are hidden in `imgui_internal.h` for this reason, and even so, if they do change, we'll make reasonable effort to document the reasoning the update path. 

In addition, Docking will only move forward with feedback from users, so the more people using it, the closer we are to a reach mergeable version. TL;DR; is totally fine to use for most users.

## Usage Guide

Also see our [[Glossary]] about Docking terminology.

#### Docking

Dock by dragging windows from their title tab or tab (hold SHIFT to disable docking)

- Dock into an existing window or node

  ![capture_docking_wiki_gifs_0001](https://user-images.githubusercontent.com/19151258/82671137-ffb64300-9c46-11ea-8e98-1a78a128882d.gif)
- Split existing node

  ![capture_docking_wiki_gifs_0000](https://user-images.githubusercontent.com/19151258/82671136-ff1dac80-9c46-11ea-8794-6220d5bad078.gif)

#### Undocking

- Undock a window from a node

  ![capture_docking_wiki_gifs_0002](https://user-images.githubusercontent.com/19151258/82671170-0d6bc880-9c47-11ea-88fb-5761d163439a.gif)
- Undock a node (all windows) from a hierarchy

  ![capture_docking_wiki_gifs_0003](https://user-images.githubusercontent.com/19151258/82671172-0e045f00-9c47-11ea-88b2-d84e18be2b6b.gif)

#### Other features

- Tab bar may be hidden

  ![capture_docking_wiki_gifs_0004](https://user-images.githubusercontent.com/19151258/92583366-e3dcb880-f29a-11ea-8a21-b503a2801c87.gif)

## Dockspace

If you want to dock window on the edge of your screen (rather than only into other windows), most application can do:
```cpp
ImGui::NewFrame();

// Create a dockspace in main viewport.
ImGui::DockSpaceOverViewport();
```
or
```cpp
ImGui::NewFrame();

// Create a dockspace in main viewport, where central node is transparent.
ImGui::DockSpaceOverViewport(0, ImGui::GetMainViewport(), ImGuiDockNodeFlags_PassthruCentralNode);
```

`DockSpaceOverViewport()` is a helper which:
- Create an invisible window covering the given viewport.
- Then submits a `DockSpace()` into it.

That's pretty much what it does.

A `DockSpace()` is an arbitrary location inside a window, where other windows may be docked into.
- Dockspaces need to be submitted _before_ any window they can host. Submit it early in your frame!
  - (because of this constraint, the implicit `"Debug"` window can not be docked into an explicit DockSpace() node, because that window is submitted as part of the part of the NewFrame() call. An easy workaround is that you can create your own implicit `"Debug##2"` window after submitting a dockspace, leave it in the window stack for anyone to use)
- Dockspaces need to be kept alive if hidden, otherwise windows docked into it will be undocked. 
  - If you have e.g. multiple tabs with a dockspace inside each tab: submit the non-visible dockspaces with `ImGuiDockNodeFlags_KeepAliveOnly`.

## Programmatically setting up docking layout (DockBuider api)

Unfortunately, there is no great API for this yet. I am sorry! I know everyone is asking for this!

- There _is_ a DockBuilder API in imgui_internal.h. **It's not great, it is unfinished, and not well documented** (you can find more examples if you search in Issues).
- An alternative is to manually create desired settings, save them using `SaveIniSettingsXXX()` function, strip the data to whatever is necessary to you and call `LoadIniSettingsXXX()`.

DockBuilder API idiomatic example:
```cpp
#include "imgui_internal.h"

ImGuiID dockspace_id = ImGui::GetID("My Dockspace");
ImGuiViewport* viewport = ImGui::GetMainViewport();

// Create settings
if (ImGui::DockBuilderGetNode(dockspace_id) == nullptr)
{
    ImGui::DockBuilderAddNode(dockspace_id, ImGuiDockNodeFlags_DockSpace);
    ImGui::DockBuilderSetNodeSize(dockspace_id, viewport->Size);
    ImGuiID dock_id_left = 0;
    ImGuiID dock_id_main = dockspace_id;
    ImGui::DockBuilderSplitNode(dock_id_main, ImGuiDir_Left, 0.20f, &dock_id_left, &dock_id_main);
    ImGuiID dock_id_left_top = 0;
    ImGuiID dock_id_left_bottom = 0;
    ImGui::DockBuilderSplitNode(dock_id_left, ImGuiDir_Up, 0.50f, &dock_id_left_top, &dock_id_left_bottom);
    ImGui::DockBuilderDockWindow("Game", dock_id_main);
    ImGui::DockBuilderDockWindow("Properties", dock_id_left_top);
    ImGui::DockBuilderDockWindow("Scene", dock_id_left_bottom);
    ImGui::DockBuilderFinish(dockspace_id);
}

// Submit dockspace
ImGui::DockSpaceOverViewport(dockspace_id, viewport, ImGuiDockNodeFlags_PassthruCentralNode);

// Submit windows
ImGui::Begin("Properties");
...
```

- I dislike this API probably even more than you. I expect to redesign this before it reaches the public API.

<img alt="DockBuilder example" src="https://github.com/user-attachments/assets/3576eac9-cc9c-43e5-b6f7-e6ce6fea9400" />

### Debugging

- Use the [Debug Log](https://github.com/ocornut/imgui/wiki/Debug-Tools#debug-log) to log docking events.
- Use the [Metrics/Debugger Window](https://github.com/ocornut/imgui/wiki/Debug-Tools#metricsdebugger-window)'s Docking section to browse internal docking data.

### More

- TODO: explain what data is persisting in .ini file, how and why.
