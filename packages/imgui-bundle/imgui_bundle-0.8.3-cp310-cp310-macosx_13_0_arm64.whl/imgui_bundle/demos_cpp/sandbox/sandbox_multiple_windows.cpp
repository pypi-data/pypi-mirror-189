#include "hello_imgui/hello_imgui.h"


int main()
{
    auto gui1 = []()
    {
        static char msg[2048] = "Hello";
        static ImVec2 size(300.f, 300.f);

        ImGui::Text("Gui1");
        ImGui::SetNextItemWidth(100.f); ImGui::SliderFloat("size.x", &size.x, 10.f, 600.f);
        ImGui::SetNextItemWidth(100.f); ImGui::SliderFloat("size.y", &size.y, 10.f, 600.f);
        ImGui::InputTextMultiline("Text", msg, 2048, size);
    };

    HelloImGui::DockableWindow w1("gui1", "", gui1);
    w1.imGuiWindowFlags |= ImGuiWindowFlags_AlwaysAutoResize;

    HelloImGui::RunnerParams params;
    params.imGuiWindowParams.showMenuBar = true;
    params.imGuiWindowParams.enableViewports = true;
    params.dockingParams.dockableWindows = {w1};

    HelloImGui::Run(params);
}
