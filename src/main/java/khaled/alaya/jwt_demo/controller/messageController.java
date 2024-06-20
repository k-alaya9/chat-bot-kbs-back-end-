package khaled.alaya.jwt_demo.controller;

import java.util.List;

import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import khaled.alaya.jwt_demo.model.chat;
import khaled.alaya.jwt_demo.model.message;
import khaled.alaya.jwt_demo.model.messageRequest;
import khaled.alaya.jwt_demo.service.messageService;
import khaled.alaya.jwt_demo.service.userJpaService;

@RequestMapping("/api/chat")
@RestController
public class messageController {

    private messageService messageService;
    private userJpaService userJpaService;
    public messageController(khaled.alaya.jwt_demo.service.messageService messageService,userJpaService userJpaService) {
        this.messageService = messageService;
        this.userJpaService=userJpaService;
    }



    @PostMapping("/message")
    public message addMessage(@RequestBody messageRequest newmessageRequest){
        return messageService.addMessage(newmessageRequest,userJpaService.loadUserByUsername(SecurityContextHolder.getContext().getAuthentication().getName()).getUsername());
    }

        @GetMapping("/{chat}")
    public List<message> geChat(@PathVariable Long chat) {
        return messageService.findByChat_id(chat);
    }
    @DeleteMapping("/message/{message}")
    public void deletedMessage(@PathVariable message message){
         messageService.deleteMessage(message);
    }

}
